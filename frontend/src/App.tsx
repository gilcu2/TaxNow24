import { TopBar } from "./TopBar";
import React from "react";
import { Outlet } from "react-router-dom";

export function App(_props: any): JSX.Element {
  return (
    <>
      <TopBar />
      <main>
        <Outlet />
      </main>
    </>
  );
}
