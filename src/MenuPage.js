import React, {Component} from 'react'
import {Carousel,Panel,Col,Thumbnail,Button,Grid,Row} from "react-bootstrap"
import './Menu.css';

class Menu extends Component {
    render() {
      return (
          <div>
        <div className="Menu">
        <Carousel>
  <Carousel.Item>
    <img width={900} height={500} alt="900x500" src ="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png" />
    <Carousel.Caption>
      <h3>First slide label</h3>
      <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
    </Carousel.Caption>
  </Carousel.Item>
  <Carousel.Item>
    <img width={900} height={500} alt="900x500" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png" />
    <Carousel.Caption>
      <h3>Second slide label</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    </Carousel.Caption>
  </Carousel.Item>
  <Carousel.Item>
    <img width={900} height={500} alt="900x500" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png" />
    <Carousel.Caption>
      <h3>Third slide label</h3>
      <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
    </Carousel.Caption>
  </Carousel.Item>
</Carousel>;
          
        </div>
        <br/>
        <div className="Popular">
        <Panel>
        <h1 className = "Title">
    Populars 
  </h1>
          <Panel.Body>Panel content</Panel.Body>
          <Grid>
  <Row>
    <Col xs={6} md={4}>
      <Thumbnail src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png" alt="242x200">
        <h3>Thumbnail label</h3>
        <p>Description</p>
        <p>
          <Button bsStyle="Buy">Buy</Button>
          
        </p>
      </Thumbnail>
    </Col>
    <Col xs={6} md={4}>
      <Thumbnail src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png" alt="242x200">
        <h3>Thumbnail label</h3>
        <p>Description</p>
        <p>
        <Button bsStyle="Buy">Buy</Button>
        </p>
      </Thumbnail>
    </Col>
    <Col xs={6} md={4}>
      <Thumbnail src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png" alt="242x200">
        <h3>Thumbnail label</h3>
        <p>Description</p>
        <p>
        <Button bsStyle="Buy">Buy</Button>
        </p>
      </Thumbnail>
    </Col>
  </Row>
</Grid>
        </Panel>
        
        </div>

</div>
      );
    }
  }
  
  export default Menu;

