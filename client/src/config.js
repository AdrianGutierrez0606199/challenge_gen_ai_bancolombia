
// The API_KEY is used to authenticate requests to the OpenAI API, in a production environment, it should be stored securely in a secret
export const AWS_API_GATEWAY_KEY = "guNfor1cga65SEnyX0mXrandi5TGyu1Y8etO6YsC";
export const BACKEND_API_URL =
  "https://7o9klj77j9.execute-api.us-east-1.amazonaws.com/";

// this key is not the true key used to authenticate requests to the OpenAI API, it is a placeholder for demonstration purposes
// the reason I wanted the application to handle the OpenAI API key is so that anyone can deploy the app and use the lambda as a router to the OpenAI API 
// but the app deploying the chatbot should assume the OpenAI API costs
export const OPENAI_API_KEY = "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";
export const DB_ARN = "arn:aws:rds:us-east-1:136942299590:cluster:database-postgre-rag-genai";
export const DB_NAME = "postgres";
export const DB_SECRET = "arn:aws:secretsmanager:us-east-1:136942299590:secret:rds!cluster-bc9df300-65e2-4498-8d98-e354f8fb1f84-IpQW8x";
export const MOVIES_TABLE = "movies_context";
export const BACKEND_API_TEST_URL =
  "https://7o9klj77j9.execute-api.us-east-1.amazonaws.com/";
export const OPENAI_EXAMPLES_URL = "https://platform.openai.com/examples/";
export const APPLICATIONS = {
  MovieChat: "MovieChat",
};
