import React from "react";
import styles from "./UpdateState.module.css";

export function UpdateState(_props: any): JSX.Element {
  return (
    <section>
      <h1>Update state</h1>
      <div className={styles.card}>
        <p>
          <label htmlFor="state-name">State name:</label>
          <input type="text" id="state-name" name="state-name" />
        </p>

        <p>
          <label htmlFor="tax-amount">Tax Amount:</label>
          <input type="number" id="tax-amount" name="tax-amount" />
        </p>
        <p>
          <button
            type="submit"
            className={`${styles.button} ${styles.buttonPrimary}`}
          >
            Update State Tax
          </button>
        </p>
      </div>
    </section>
  );
}
