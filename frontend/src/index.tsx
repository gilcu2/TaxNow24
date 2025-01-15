import React from "react";
import ReactDOM from "react-dom";
import "./index.module.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { App } from "./App";
import { UpdateState } from "./UpdateState";

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />}>
          <Route index element={<UpdateState />} />
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById("root")
);
