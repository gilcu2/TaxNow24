import { render, screen } from "@testing-library/react";
import React from "react";
import { UpdateState } from "./UpdateState";

describe("CreateState component", () => {
  it("should render", () => {
    render(<UpdateState />);

    const taxAmountInput = screen.getByLabelText(/tax amount/i);
    const stateNameInput = screen.getByLabelText(/state name/i);
    const submitButton = screen.getByText(/update state tax/i);

    expect(taxAmountInput).toBeInTheDocument();
    expect(stateNameInput).toBeInTheDocument();
    expect(submitButton).toBeInTheDocument();
  });
});
