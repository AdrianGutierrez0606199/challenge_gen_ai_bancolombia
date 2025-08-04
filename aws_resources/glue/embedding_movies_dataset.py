import os
import openai
from openai import OpenAI
import pandas as pd
import sys
import time
from awsglue.utils import getResolvedOptions
import boto3
import json

# Define the parameters you expect
try:
    args = getResolvedOptions(sys.argv, ['OPENAI_API_KEY','DB_ARN', 'DB_SECRET', 'DB_NAME','MOVIES_DATA_PATH','MOVIES_TABLE'])

    openai_api_key = args["OPENAI_API_KEY"]
    db_arn = args["DB_ARN"]
    db_name = args["DB_NAME"]
    db_secret = args["DB_SECRET"]
    input_file_path = args["MOVIES_DATA_PATH"]
    movies_table = args["MOVIES_TABLE"]
except Exception as e:
    print(f"Error retrieving parameters: {e}")
    raise ValueError(f"Missing required parameters: {e}")

BATCH_SIZE = 50  # Define the batch size for processing


def batch_insert_movies_vector_1536(movies_data):
    """Insert multiple movies with VECTOR(1536) embeddings using RDS Data API batch execute"""
    
    client = boto3.client('rds-data')
    
    cluster_arn = db_arn
    secret_arn = db_secret
    database_name = db_name
    
    # Prepare parameter sets for batch execution
    parameter_sets = []
    
    for movie in movies_data:
        # Validate embedding vector length
        if len(movie['embedding']) != 1536:
            raise ValueError(f"Embedding vector for '{movie['title']}' must be exactly 1536 dimensions, got {len(movie['embedding'])}")
        
        # Convert embedding to PostgreSQL vector format
        vector_string = '[' + ','.join(map(str, movie['embedding'])) + ']'
        
        parameter_set = [
            {'name': 'title', 'value': {'stringValue': movie['title']}},
            {'name': 'image', 'value': {'stringValue': movie['image']}},
            {'name': 'plot', 'value': {'stringValue': movie['plot']}},
            {'name': 'embedding', 'value': {'stringValue': vector_string}}
        ]
        parameter_sets.append(parameter_set)
    
    try:
        response = client.batch_execute_statement(
            resourceArn=cluster_arn,
            secretArn=secret_arn,
            database=database_name,
            sql=f"""
                INSERT INTO {movies_table} (title, image, plot, embedding) 
                VALUES (:title, :image, :plot, :embedding::vector(1536))
            """,
            parameterSets=parameter_sets
        )
        
        print(f"Successfully inserted {len(movies_data)} movies with VECTOR(1536) embeddings in batch")
        return response
        
    except Exception as e:
        print(f"Batch vector insert error: {e}")
        raise

try:
    # Configura la API Key
    openai.api_key = openai_api_key

    # client connection to rds-data
    client = boto3.client("rds-data")

except Exception as e:
    print(f"Error setting up OpenAI or RDS Data API client: {e}")
    raise Exception(f"Failed to set up clients: {e}")

# Leer CSV desde s3
try:
    df = pd.read_csv(input_file_path)
except Exception as e:
    print(f"Error reading CSV file from S3: {e}")
    raise Exception(f"Failed to read CSV file: {e}")

try:
    # create the table if it does not exist
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {movies_table} (
        id SERIAL PRIMARY KEY,
        title TEXT,
        image TEXT,
        plot TEXT,
        embedding VECTOR(1536)
    );
    """
    response = client.execute_statement(
        resourceArn=db_arn,
        secretArn=db_secret,
        database=db_name,
        sql=create_table_query
    )
    print(response)
except Exception as e:
    print(f"Error creating table {movies_table} or accessing the database {db_name}: {e}")
    raise Exception(f"Failed to create table: {e}")

# create variables for batch processing
batch_counter = 0
embeddings = []

try:
    for _, row in df.iterrows():
        
        ## in case I would like to get a description of the image used (not implemented because of the token cost)
        # try:
        #     response = openai.chat.completions.create(
        #         model="gpt-4o-mini",  # or gpt-4o
        #         messages=[
        #             {"role": "user", "content": [
        #                 {"type": "text", "text": f"Describe this poster of the movie'{row['title']}'"},
        #                 {"type": "image_url", "image_url": {"url": row['image']}}
        #             ]}
        #         ]
        #     )
        # except:
        #     time.sleep(60)
        #     response = openai.chat.completions.create(
        #         model="gpt-4o-mini",  # or gpt-4o
        #         messages=[
        #             {"role": "user", "content": [
        #                 {"type": "text", "text": f"Describe this poster of the movie'{row['title']}'"},
        #                 {"type": "image_url", "image_url": {"url": row['image']}}
        #             ]}
        #         ]
        #     )
        #     print("image detection response:",response.choices[0].message.content)
        # print("Total tokens:", response.usage.total_tokens)
        text = f"Movie Title: {row['title']}\nMovie Plot: {row['plot']}\nMovie image URL:{row['image']}"
        print(text)
        try:
            resp = openai.embeddings.create(
                model="text-embedding-ada-002",
                input=text
            )
        except Exception as e:
            time.sleep(60)
            print("error retrieving response:",e)
            resp = openai.embeddings.create(
                model="text-embedding-ada-002",
                input=text
            )
        
        vector = resp.data[0].embedding
        embeddings.append({"title": row["title"], "image": row["image"], "plot": row["plot"], "embedding": vector})
        batch_counter += 1
        if batch_counter == BATCH_SIZE:
            # Insert batch into the database incrementally so if the process fails, we don't lose all the data
            response = batch_insert_movies_vector_1536(embeddings)
            embeddings = []  # Reset the batch
            batch_counter = 0
            print("Batch inserted successfully, waiting for next batch...",response)

    if embeddings:
        # Insert any remaining movies in the last batch
        response = batch_insert_movies_vector_1536(embeddings)
        print("Final batch inserted successfully", response)
except Exception as e:
    print(f"Error embedding the data from to {movies_table}: {e}")
    raise Exception(f"Failed to embed data and upload to {movies_table}: {e}")

# End the job execution
print("embeddings generados y guardados en Aurora PostgreSQL")
