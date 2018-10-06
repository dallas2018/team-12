import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import './index.css';
import App from './App';
import Login from './Login/index';
//import Menu from './MenuPage';
import Navigation from './navigation';


import * as serviceWorker from './serviceWorker';

ReactDOM.render(<Navigation/>,document.getElementById('Header'));
ReactDOM.render(
<Router>
    <div>
        <Route path="/" exact component={App} />
        <Route path="/login" exact component={Login} />
    </div>
</Router>,
document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
