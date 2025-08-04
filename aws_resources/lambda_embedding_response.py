import os
import openai
import sys
import time
import boto3
import json
import requests

def get_embedding(text, api_key):
    """Get embedding for the input text using OpenAI API."""
    url = "https://api.openai.com/v1/embeddings"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "input": text,
        "model": "text-embedding-ada-002"
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def lambda_handler(event, context):
    try:
        event = json.loads(event['body'])
    except Exception as e:
        pass
    print("input json:",event)
    openai_api_key = event["OPENAI_API_KEY"]
    db_arn = event["DB_ARN"]
    db_name = event["DB_NAME"]
    db_secret = event["DB_SECRET"]
    movies_table = event["MOVIES_TABLE"]
    text = event["text"]

    #authenticate with OpenAI
    openai.api_key = openai_api_key

    # API call to openai endpoint to get the embedding
    response = get_embedding(text, openai_api_key)
    # resp = openai.embeddings.create(
    #         model="text-embedding-ada-002",
    #         input=text
    #     )

    # Extract the embedding from the response
    vector = response['data'][0]['embedding']

    # Convert embedding to PostgreSQL vector format
    vector_string = '[' + ','.join(map(str, vector)) + ']'

    # query to find similar movies
    query = f"SELECT title, plot, image FROM {movies_table} ORDER BY embedding <-> :embedding::vector(1536) LIMIT 1"

    # send the query to the database
    client = boto3.client('rds-data')
    response = client.execute_statement(
        resourceArn=db_arn,
        secretArn=db_secret,
        database=db_name,
        sql=query,
        parameters=[
            {
                'name': 'embedding',
                'value': {'stringValue': vector_string}
            }
        ]
    )

    # add history to the prompt so that the LLM has memory of the conversation
    chat_history_list = []
    chat_history = event["chat_history"]

    # skip the first two messages in the chat history as they are usually system prompts or initial greetings
    for i, message in enumerate(chat_history):
        if i>=2:
            chat_history_list.append({"role": message['sender'], "content": message['message']})

    # system message for the chatbot
    system_message_1 = {"role": "system", "content": "Eres un microservicio siendo llamado por otro chatbot que esta usando RAG para darte contexto, sin embargo, tambien se te esta brindando el historial del chat y no en todos los casos debes usar el contexto. Necesito que tu respuesta siempre sea en formato html compatible con react; Sin embargo, es obligatorio que en esos casos donde venga una imagem, esta sea en formato <a href= y no <img src. Ademas, en todos los casos debes responder en el mismo idioma que te hicieron la pregunta y en lenguaje natural ya que el chat no va a hacer procesamiento adicional a tu respuesta"}

    # Extract the records from the response
    context_string_list = [str({'titulo':record[0]["stringValue"],'descripcion':record[1]["stringValue"],'url del poster a la pelicula':record[2]["stringValue"]}) for record in response['records']]
    # create the prompt to send to the LLM
    prompt = f"Contexto:\n" + "\n".join(context_string_list) + f"\nPregunta: {text}\nRespuesta:"
    response = openai.ChatCompletion.create(model="gpt-4", messages= [system_message_1] + chat_history_list + [{"role":"user","content":prompt}])
    print("messages:", [system_message_1] + chat_history_list + [{"role":"user","content":prompt}])

    return json.dumps(response)
