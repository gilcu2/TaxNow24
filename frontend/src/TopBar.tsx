import React from "react";
import styles from "./TopBar.module.css";
import { Link } from "react-router-dom";

export function TopBar(_props: any): JSX.Element {
  return (
    <header className={styles.topBar}>
      <div className={styles.maxWidth}>
        <div className={styles.logo}>TaxNow24</div>
        <nav>
          <Link className={styles.navigationItem} to="/">
            Update State
          </Link>
        </nav>
      </div>
    </header>
  );
}
