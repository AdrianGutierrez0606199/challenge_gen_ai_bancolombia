//
//
import React from "react";
import "./Component.css";
const AboutPage = () => {
  return (
    <div className="about-page">
      <div className="app-stack">
        <h2>Application Stack</h2>
        <p>
          Este código implementa un chatbot para el reto de IA generativa de Bancolombia, el cual permite a los usuarios interactuar con un modelo de Lenguage natural para no solo obtener informacion del modelo, sino tambien, informacion adicional alimentada por medio de Retrieval Augmented Generation
          para resolver preguntas frecuentes respecto a una serie de peliculas cargadas en la base de datos.
          La aplicacion esta construida con {" "}
          <a href="https://react.dev/" target="_blank" rel="noreferrer">
            React
          </a>{" "}
          utilizando{" "}
          <a
            href="https://www.npmjs.com/package/@chatscope/chat-ui-kit-react"
            target="_blank"
            rel="noreferrer"
          >
            @chatscope/chat-ui-kit-react
          </a>{" "}
          y{" "}
          <a
            href="https://www.npmjs.com/package/react-pro-sidebar"
            target="_blank"
            rel="noreferrer"
          >
            react-pro-sidebar.
          </a>{" "}
          Esta corriendo en{" "}
          <a href="https://aws.amazon.com/" target="_blank" rel="noreferrer">
            AWS,
          </a>{" "}
          en arquitectura sin servidor e integrada a{" "}
          <a
            href="https://platform.openai.com/docs/api-reference?lang=python"
            target="_blank"
            rel="noreferrer"
          >
            OpenAI Python API
          </a>
          .
        </p>
        <a
          href="https://github.com/AdrianGutierrez0606199/challenge_gen_ai_bancolombia"
          target="_blank"
          rel="noreferrer"
        >
          <img src="/Bancolombia_test.jpg" />
        </a>
        <div>
          Accede al Código del reto aca:{" "}
          <a
            href="https://github.com/AdrianGutierrez0606199/challenge_gen_ai_bancolombia"
            target="_blank"
            rel="noreferrer"
          >
            https://github.com/AdrianGutierrez0606199/challenge_gen_ai_bancolombia
          </a>
        </div>
      </div>
    </div>
  );
};

export default AboutPage;
