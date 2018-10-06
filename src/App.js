import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {Elements, StripeProvider} from 'react-stripe-elements';
import CheckoutForm from './CheckoutForm';


class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">        
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>                    
        </header>

        <StripeProvider apiKey="pk_test_TYooMQauvdEDq54NiTphI7jx">
        <div className="example">
          <h1>React Stripe Elements Example</h1>
          <Elements>
            <CheckoutForm />
          </Elements>
        </div>
      </StripeProvider>
      </div>

      
    );
  }
}

export default App;
