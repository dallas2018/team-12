import React ,{Component} from 'react';
import {Nav,
    Navbar,
NavItem, } from 'react-bootstrap'

class Navigation extends Component{
    render(){
        return(
          <Navbar inverse collapseOnSelect>
  <Navbar.Header>
    
    <Navbar.Toggle />
  </Navbar.Header>
  <Nav>
    <NavItem eventKey={1} href="/">
      Home
    </NavItem>
    <NavItem eventKey={2} href="/features">
      Featured  
    </NavItem>
    <NavItem eventKeys={3} href="/Items/">
      Items
    </NavItem>
    <NavItem eventKey={4} href="/Login/">
      Sign Up/Log In
    </NavItem>
    <NavItem eventKey={5} href="/donate">
    Donate
    </NavItem>
    <NavItem eventKey={6} href="https://neonto.cloud/preview/7ygawyyv/">
    Mobile Site (Test)
    </NavItem>
    
  </Nav>
        </Navbar>);
    }
}

export default Navigation