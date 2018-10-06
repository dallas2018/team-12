import React,{Component} from 'react';
import {Button,FormGroup,FormControl,ControlLabel,Form} from 'react-bootstrap';

class buy extends Component{

    constructor(props, context) {
        super(props, context);
    
        this.handleChange = this.handleChange.bind(this);
    
        this.state = {
          value: '',
          cvs:''
        };
      }

    getValidationState() {
        const length = this.state.value.length;
        if (length > 10) return 'success';
        else if (length > 5) return 'warning';
        else if (length > 0) return 'error';
        return null;
      }
    
      handleChange(e) {
        this.setState({ value: e.target.value });
      }    

    render(){
        return(
            <div>
            <h1>Price: $20</h1>
                <Form inline>
                <FormGroup controlId="formInlineName">
                    <ControlLabel>Credit Card</ControlLabel>{' '}
                    <FormControl type="text" />
                </FormGroup>{' '}
                <FormGroup controlId="formInlineEmail">
                    <ControlLabel>CSV</ControlLabel>{' '}
                    <FormControl type="password" />
                </FormGroup>{' '}
                </Form>
            <Button href = "/checkout">Submit</Button>
            </div>
        );
    }
};

export default buy;