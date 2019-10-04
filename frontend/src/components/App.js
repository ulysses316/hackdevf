/*
__Seed builder__v1.0
*/

import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect
} from "react-router-dom";

import Examples from "examples/Examples";

import cx from "classnames";
import styles from "resources/css/App.module.css";
import Login from "examples/general/auth/Login";
import Feed from "./Feed";
import Perfil from "./Perfil";

function App(props) {
  return (
    <div className={styles.module}>
      <Router>
        <Switch>
          <Route path="/login" component={Login} />
          <Route path="/feed" component={Feed} />
          <Route path="/perfil" component={Perfil} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
