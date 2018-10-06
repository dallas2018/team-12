import React ,{Component} from 'react';
import {Nav,
    Navbar,
NavItem,
NavDropdown,
MenuItem} from 'react-bootstrap'
class Navigation extends Component{
    render(){
        return(
        <Navbar>
  <Navbar.Header>
    
  </Navbar.Header>
  <Nav>
    <NavItem eventKey={1} href="/">
      Home
    </NavItem>
    <NavItem eventKey={2} href="/features">
      Features
    </NavItem>
    <NavItem eventKey={3} href="/Items/">
      Items
    </NavItem>
    <NavItem eventKey={4} href="/Login/">
      Sign Up/Log In
    </NavItem>
    <NavDropdown eventKey={3} title="Dropdown" id="basic-nav-dropdown">
      <MenuItem eventKey={3.1}>Action</MenuItem>
      <MenuItem eventKey={3.2}>Another action</MenuItem>
      <MenuItem eventKey={3.3}>Something else here</MenuItem>
      <MenuItem divider />
      <MenuItem eventKey={3.4}>Separated link</MenuItem>
    </NavDropdown>
  </Nav>
        </Navbar>);
    }
}

export default Navigation