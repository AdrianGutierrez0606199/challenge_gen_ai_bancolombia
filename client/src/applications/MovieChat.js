// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_API_KEY,
  DB_ARN,
  DB_NAME,
  DB_SECRET,
  MOVIES_TABLE
} from "../config";

const SLUG = "load_movies_data";

const MovieChat = {
  sidebar_title: "Chat sobre Peliculas",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  api_openai_key: OPENAI_API_KEY,
  db_arn: DB_ARN,
  db_name: DB_NAME,
  db_secret: DB_SECRET,
  movies_table: MOVIES_TABLE,
  app_name: "Marv el bot de Peliculas",
  assistant_name: "Marv",
  avatar_url: "/applications/SarcasticChat/Marv.svg",
  background_image_url: "/applications/SarcasticChat/SarcasticChat-bg.png",
  welcome_message: `¡Hola! 👋 Soy Marv, tu compañero cinéfilo digital.\n\nEstoy aquí para ayudarte a explorar nuestro catálogo de películas más representativas. Ya sea que busques una recomendación, quieras conocer detalles sobre una película específica, o simplemente tengas curiosidad sobre el mundo del cine, ¡estoy listo para ayudarte!\n\nPregúntame lo que quieras sobre películas y te responderé con la información más precisa que tenga disponible.\n\n¿Qué te gustaría descubrir sobre el cine hoy? 🎬`,
  example_prompts: ["¿En qué consiste la película Echoes of Tomorrow? Muestre la respuesta indicando el contexto de la pregunta. Ejemplo: Esta película consiste en...", "En la película Enigma cual es el nombre del protagonista y quien interpreta al agente de la CIA.","¿Cuál es el nombre de la película, donde los humanos y las IA’s coexisten y tienen una batalla por el control de la realidad?","Muestre la imagen relacionada a la película Stellar Odyssey"],
  placeholder_text: `Preguntale algo a Marv`,
  info_url: `https://github.com/AdrianGutierrez0606199/challenge_gen_ai_bancolombia`,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: false,
  uses_langchain: false,
  uses_memory: true,
};

export default MovieChat;
