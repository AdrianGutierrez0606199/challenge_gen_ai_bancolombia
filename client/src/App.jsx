// React code
import React from "react";
import { useState } from "react";

// Third party components
import { Sidebar, Menu, MenuItem, SubMenu } from "react-pro-sidebar";
import {
  ContainerLayout,
  SidebarLayout,
  ContentLayout,
} from "./components/Layout/";
import {
  FaInfo,
  FaTheaterMasks,
} from "react-icons/fa";

// Our code
import "./App.css";
import ChatApp from "./components/chatApp/Component";
import AboutPage from "./components/about/Component";
import { APPLICATIONS } from "./config";

import MovieChat from "./applications/MovieChat";


const Footer = () => {
  return (
    <div className="footer hide-small">
      <p>
        {" "}
        <a href="https://openai.com/">  
          <img src="openai-logo.svg" /> OpenAI Python API
        </a>{" "}
        |{" "}
        <a href="https://react.dev/">
          <img src="/react-logo.svg" /> React
        </a>{" "}
        |{" "}
        <a href="https://aws.amazon.com/">
          <img src="/aws-logo.svg" />
        </a>{" "}
        |{" "}
        <a
          href="https://github.com/AdrianGutierrez0606199/challenge_gen_ai_bancolombia"
          target="_blank"
          rel="noreferrer"
        >
          <img src="/github-logo.svg" /> Source code
        </a>
      </p>
    </div>
  );
};

const App = () => {
  const [selectedItem, setSelectedItem] = useState(
    APPLICATIONS.FunctionCalling,
  );

  const handleItemClick = (item) => {
    setSelectedItem(item);
  };
  return (
    <div className="App">
      <h1 className="app-title hide-small">Chatbot Reto Bancolombia GenAI</h1>
      <ContainerLayout>
        <SidebarLayout className="hide-small">
          <div style={{ display: "flex", height: "100%", minHeight: "400px" }}>
            <Sidebar backgroundColor="#1d5268">
              <Menu
                menuItemStyles={{
                  button: ({ level, active, disabled }) => {
                    // only apply styles on first level elements of the tree
                    if (level === 0)
                      return {
                        color: disabled ? "gray" : "lightgray",
                        backgroundColor: active ? "#eecef9" : undefined,
                      };
                  },
                }}
              >
                <a href="https://www.bancolombia.com/personas" target="_blank" rel="noreferrer">
                  <img
                    src="/Bancolombia_logo.png"
                    alt="Bancolombia Logo"
                    className="app-logo"
                    style={{ position: "absolute", top: 0, left: 20 }}
                  />
                </a>
                <h5 className="sample-applications">Chatbot de Peliculas con RAG</h5>
                <SubMenu label="Chatbots" defaultOpen icon={<FaTheaterMasks />}>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.MovieChat)}
                  >
                    {MovieChat.sidebar_title}
                  </MenuItem>
                </SubMenu>
                <hr />
                <MenuItem
                  icon={<FaInfo />}
                  onClick={() => handleItemClick("AboutPage")}
                >
                  Documentación
                </MenuItem>
              </Menu>
            </Sidebar>
          </div>
        </SidebarLayout>
        <ContentLayout>
          {selectedItem === "AboutPage" && <AboutPage />}

          {selectedItem === APPLICATIONS.MovieChat && (
            <ChatApp {...MovieChat} />
          )}
        </ContentLayout>
      </ContainerLayout>
      <Footer />
    </div>
  );
};

export default App;
