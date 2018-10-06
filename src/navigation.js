import React ,{Component} from 'react';
import {Nav,
    Navbar,
NavItem,
NavDropdown,pullRight,
MenuItem} from 'react-bootstrap'
class Navigation extends Component{
    render(){
        return(
          <Navbar inverse collapseOnSelect>
  <Navbar.Header>
    
    <Navbar.Toggle />
  </Navbar.Header>
  <Navbar.Collapse>
    <Nav>
      <NavItem eventKey={1} href="/">
        Home
      </NavItem>
      <NavItem eventKey={2} href="/features/">
        Features
      </NavItem>
    </Nav>
    <Nav>
      <NavItem eventKey={4} href="/login/">
        Sign Up/Login
      </NavItem>      
    </Nav>
    
  </Navbar.Collapse>
</Navbar>
        );
    }
}

export default Navigation