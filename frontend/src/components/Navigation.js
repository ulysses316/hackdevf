import React from "react";
import cx from "classnames";
import { Link } from "react-router-dom";

export default function Navigation() {
  return (
    <div>
      <nav className={cx("navbar navbar-expand-lg navbar-light bg-light")}>
        <a className={cx("navbar-brand")} href="#">
          DoggyAdopt
        </a>
        <button
          className={"navbar-toggler"}
          type="button"
          data-toggle="collapse"
          data-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className={cx("navbar-toggler-icon")}></span>
        </button>
        <div className={cx("collapse navbar-collapse")} id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item active">
              <Link to="/feed">
                <a className="nav-link" href="#">
                  Feed
                </a>
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/perfil">
                <a className="nav-link" href="#">
                  Perfil
                </a>
              </Link>
            </li>
          </ul>
        </div>
      </nav>
    </div>
  );
}
