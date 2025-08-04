[![OpenAI](https://a11ybadges.com/badge?logo=openai)](https://platform.openai.com/)
[![Amazon AWS](https://a11ybadges.com/badge?logo=amazonaws)](https://aws.amazon.com/)
[![ReactJS](https://a11ybadges.com/badge?logo=react)](https://react.dev/)

# React Client Application

Este código implementa un chatbot para el reto de IA generativa de Bancolombia, que permite a los usuarios interactuar con un modelo de lenguaje natural para obtener información tanto del modelo como de una base de conocimiento adicional, alimentada mediante Retrieval Augmented Generation (RAG), resolviendo preguntas frecuentes sobre una serie de películas cargadas en la base de datos.

La aplicación está construida con [React](https://react.dev/), utilizando los paquetes [@chatscope/chat-ui-kit-react](https://www.npmjs.com/package/@chatscope/chat-ui-kit-react) y [react-pro-sidebar](https://www.npmjs.com/package/react-pro-sidebar).

Está desplegada en [AWS](https://aws.amazon.com/) bajo una arquitectura serverless e integrada con la [OpenAI Python API](https://platform.openai.com/docs/api-reference?lang=python).

## Getting Started

```console
make client-init
make client-run
```

## Architecture

- [Vite](https://vitejs.dev/)
- [React](https://react.dev/)
- [Chat UI Kit React](https://www.npmjs.com/package/@chatscope/chat-ui-kit-react)
- [React Pro Sidebar](https://www.npmjs.com/package/react-pro-sidebar)
- **AWS Serverless REST API**

## Requirements

- React 16.8+
- node 20.8+
- npm 10.1+

## Vite Scripts for React

In the project directory, you can run:

### `npm run dev`

Corre la aplicacion en mode de desarorllo en la maquina local

### `npm run build`

Builds the app for production to the `dist` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).
