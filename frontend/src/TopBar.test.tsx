import { render, screen } from "@testing-library/react";
import React from "react";
import { TopBar } from "./TopBar";
import { MemoryRouter } from "react-router-dom";

describe("TopBar component", () => {
  it("should render with navigation items", () => {
    render(
      <MemoryRouter>
        <TopBar />
      </MemoryRouter>
    );

    const createStateNavigation = screen.getByText(/update state/i);

    expect(createStateNavigation).toBeInTheDocument();
  });
});
