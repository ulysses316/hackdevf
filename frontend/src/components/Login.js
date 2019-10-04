<<<<<<< HEAD
/*
__Seed builder__v1.0
*/

import React from 'react';
import Examples from 'examples/Examples';

import cx from 'classnames';
import styles from 'resources/css/App.module.css';

function App(props)
{
  return (
    <form>
      <div class="form-group">
        <label for="exampleFormControlInput1">User name</label>
        <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="User">
        <label for="exampleFormControlInput1">Contraseña</label>
        <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
        <button type="submit" class="btn btn-primary mb-2">Confirm identity</button>
    </div>
  </form>
  );
}

export default Login;
