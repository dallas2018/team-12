import React,{Component} from 'react';
import {Row,Col,Thumbnail,Grid} from 'react-bootstrap';
import './Feature.css';

class Feature extends Component{
    render(){
        return(
        <div>
    <Grid>
           <Row>
    <Col xs={6} md={3}>
      <Thumbnail className="Thumbnail" href="#" alt="171x180" src="https://cdn-image.realsimple.com/sites/default/files/styles/portrait_435x518/public/1527198293/best%20beauty%20products%20and%20must%20haves%20of%20all%20time.jpg?itok=mp4Ks9KD"/>
    </Col>
    <Col xs={6} md={3}>
      <Thumbnail className="Thumbnail" href="#" alt="171x180" src="http://cdn.shopify.com/s/files/1/0100/3792/products/SharkTankScented_grande.jpg?v=1538190094"  />
    </Col>
    <Col xs={6} md={3}>
      <Thumbnail className="Thumbnail" href="#" alt="171x180" src="http://geekologie.com/2018/04/16/heinz-mayochup.jpg" />
    </Col>
  </Row>
  </Grid>
  <Grid>
    <Row>
    <Col xs={6} md={3}>
      <Thumbnail className="Thumbnail" href="#" alt="171x180" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTipXt3_ynYjuiltUE0KRJjWxcsiRXy2eVdbQGIyp1fOSPP18Hh" />
    </Col>
    <Col xs={6} md={3}>
      <Thumbnail className="Thumbnail"  href="#" alt="171x180" src="https://images-na.ssl-images-amazon.com/images/I/61BeXNDwpcL._SY300_QL70_.jpg"  />
    </Col>
    <Col xs={6} md={3}>
      <Thumbnail className="Thumbnail" href="#" alt="171x180" src="http://geekologie.com/2018/04/16/heinz-mayochup.jpg" />
    </Col>
  </Row>
</Grid> 
        </div>   
        );
    }
};

export default Feature;