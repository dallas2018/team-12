import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import NavBar from './navigation.js';


class App extends Component {
  render() {
    return (
      <div className="App">
        <NavBar/>
        <header className="App-header">
        
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          
            
           
           
            
          
          <button >LogIn</button>

          
        </header>
      </div>
    );
  }
}

export default App;
