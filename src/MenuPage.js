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
    <img width={600} height={500} alt="900x500" src ="https://slack-imgs.com/?c=1&url=https%3A%2F%2Fcdn-image.realsimple.com%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Fportrait_435x518%2Fpublic%2F1527198293%2Fbest%2520beauty%2520products%2520and%2520must%2520haves%2520of%2520all%2520time.jpg%3Fitok%3Dmp4Ks9KD" />
    <Carousel.Caption className="Caption">
      <h3>First slide label</h3>
      <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
    </Carousel.Caption>
  </Carousel.Item>
  <Carousel.Item>
    <img width={600} height={500} alt="900x500" src="https://slack-imgs.com/?c=1&url=https%3A%2F%2Fcdn2.stylecraze.com%2Fwp-content%2Fuploads%2F2014%2F02%2FBest-Popular-Hair-Care-Products-Available-In-India.jpg" />
    <Carousel.Caption className="Caption">
      <h3>Second slide label</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    </Carousel.Caption>
  </Carousel.Item>
  <Carousel.Item>
    <img width={900} height={500} alt="900x500" src="https://i5.walmartimages.com/asr/407a9e0e-0d71-4676-a2aa-0894bcaee5a1_1.43e2cf366f595a6414b72dac06558ba3.jpeg" />
    <Carousel.Caption className="Caption">
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
      <Thumbnail className="products" src="https://i5.walmartimages.com/asr/407a9e0e-0d71-4676-a2aa-0894bcaee5a1_1.43e2cf366f595a6414b72dac06558ba3.jpeg" alt="242x200">
        
        <p>
          <Button bsStyle="Buy">Buy</Button>
          
        </p>
      </Thumbnail>
    </Col>
    <Col xs={6} md={4}>
      <Thumbnail className="products2" src="https://images.offerup.com/AUNlvG7MlormTS3hg7we7mhHMLI=/600x800/ba3d/ba3d1fd609aa4f3a9aa44dd2ade4f033.jpg" alt="242x200">
        
        <p>
        <Button bsStyle="Buy">Buy</Button>
        </p>
      </Thumbnail>
    </Col>
    <Col xs={6} md={4}>
      <Thumbnail className="products3" src="http://getdrawings.com/image/skinny-jeans-drawing-53.jpg" alt="242x200">
        
        <p>
        <Button bsStyle="Buy" frameBorder='true'>Buy</Button>
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

