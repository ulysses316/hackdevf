import React from "react";
import cx from "classnames";
import { Link } from "react-router-dom";
import Navigation from "./Navigation";

export default function Feed() {
  return (
    <div>
      <div>
        <Navigation />
      </div>
      <div className="container">
        <div className="row">
          <div className="column">
            <div className="card" style="width: 18rem;">
              <img src="..." className="card-img-top" alt="..." />
              <div className="card-body">
                <h5 className="card-title">Card title</h5>
                <p className="card-text">
                  Some quick example text to build on the card title and make up
                  the bulk of the card's content.
                </p>
                <a href="#" className="btn btn-primary">
                  Go somewhere
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  const loadPerritos = perritos => {
    return <div>Perrito</div>;
  };
}
