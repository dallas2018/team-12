import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import './index.css';


import Features from './Features/index';
import Login from './Login/index';
import Menu from './MenuPage';
import Navigation from './navigation';
import Donation from './Donation';


import * as serviceWorker from './serviceWorker';

ReactDOM.render(<Navigation/>,document.getElementById('Header'));
ReactDOM.render(
<Router>
    <div>
        <Route path="/" exact component={Menu} />
        <Route path="/login" exact component={Login} />
        <Route path="/features" exact component ={Features}/>
        <Route path = "/donate" exact component = {Donation}/>
    </div>
</Router>,
document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
