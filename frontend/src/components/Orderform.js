import React, { useState } from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import SwipeableViews from 'react-swipeable-views';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import {Tabs, Tab, Grid, Button, Radio, RadioGroup, FormControl, FormControlLabel, FormLabel, Select, MenuItem, InputLabel} from '@material-ui/core';
import Title from './Title';
import axios from 'axios';
import { useStateValue } from '../StateProvider'; 


function preventDefault(event) {
  event.preventDefault();
}

const useStyles = makeStyles({
  orderContext: {
    flex: 1,
  },
});

function TabPanel(props){
  const {children,value,index} = props;
  return(<div>
    {value===index && (
      <div>{children}</div>
    )}
  </div>)
}

export default function Orderform() {
  
  const [{ user, stockPrice }, dispatch] = useStateValue();
  const classes = useStyles();

  const [value, setValue] = useState(0);
  const [qty, setQty] = useState();
  const [price, setPrice] = useState();
  const [radio, setRadio] = useState('m');
  const [security, setSecurity] = React.useState(0);

  const handleSelectChange = (event) => {
    setSecurity(event.target.value);
    dispatch({
      type: 'SET_USER',
      user: event.target.value,
  });
  };

  const handleTabChange = (event, newValue) => {
    setValue(newValue);
  };

  const handleChangeIndex = (index) => {
    setValue(index);
  };

  const handleRadioChange = (event) => {
    setRadio(event.target.value);
  };

  const handleSubmit = () => {
    const securities = ['APP1984','MIC1990','IBM1950','XER1960','PIX1991'];
    const postObject = {
      'ISIN' : securities[security],
      'id':10,
      'price': radio==='m'?stockPrice:price,
      'qty': qty,
      'aon': 'n',
      'identifier': 10,
      'BOS': value?'s':'b',
      'LOM': radio
    }
    axios.post('/addManualorder', postObject).then(response=>{ console.log(response)});
  }

  return (
    <React.Fragment>
      <Title>Place Order</Title>
      <Tabs
        value={value}
        indicatorColor="primary"
        textColor="primary"
        onChange={handleTabChange}
        aria-label="tabs example"
        variant="fullWidth"
      >
    <Tab label="Buy" />
    <Tab label="Sell" />
  </Tabs>
  <SwipeableViews
        axis='x'
        index={value}
        onChangeIndex={handleChangeIndex}
      >
      <TabPanel value = {value} index={0}>
      <FormControl margin="normal" variant="outlined" style={{minWidth : 230, textAlign:"left"}} >
        <InputLabel id="demo-simple-select-outlined-label">Security</InputLabel>
        <Select
          labelId="demo-simple-select-outlined-label"
          id="demo-simple-select-outlined"
          value={security}
          onChange={handleSelectChange}
          label="Security"
        >
          <MenuItem value={0}>Apple</MenuItem>
          <MenuItem value={1}>Microsoft</MenuItem>
          <MenuItem value={2}>IBM</MenuItem>
          <MenuItem value={3}>Xerox</MenuItem>
          <MenuItem value={4}>Pixar</MenuItem>
        </Select>
      </FormControl>
      <Grid >
        <TextField onChange={event => setQty(event.target.value)} margin="normal" id="outlined-basic" label="Quantity" variant="outlined" value={qty} />
        <TextField onChange={event => setPrice(event.target.value)} margin="normal" id="outlined-basic" label="Price" variant="outlined" value={radio==='m'?stockPrice:price}/>  
        <FormControl component="fieldset">
          <RadioGroup row aria-label="LOM" name="LOM" value={radio} onChange={handleRadioChange}>
            <FormControlLabel value="m" control={<Radio color="primary"/>} label="Market" />
            <FormControlLabel value="l" control={<Radio />} label="Limit" />
          </RadioGroup>
        </FormControl>    
          </Grid>
          <Button onClick={handleSubmit} variant="contained" color="primary" style={{marginTop:8, minWidth: 270, borderRadius:5, fontSize:15}}>
            Buy
          </Button>
      </TabPanel>
      <TabPanel value = {value} index={1}>
      <FormControl margin="normal" variant="outlined" style={{minWidth : 230, textAlign:"left"}}>
        <InputLabel id="demo-simple-select-outlined-label">Security</InputLabel>
        <Select
          labelId="demo-simple-select-outlined-label"
          id="demo-simple-select-outlined"
          value={security}
          onChange={handleSelectChange}
          label="Security"
        >
          <MenuItem value={0}>Apple</MenuItem>
          <MenuItem value={1}>Microsoft</MenuItem>
          <MenuItem value={2}>IBM</MenuItem>
          <MenuItem value={3}>Xerox</MenuItem>
          <MenuItem value={4}>Pixar</MenuItem>
        </Select>
      </FormControl>
      <Grid >
        <TextField onChange={event => setQty(event.target.value)} margin="normal" id="outlined-basic" label="Quantity" variant="outlined" value={qty}/>
        <TextField onChange={event => setPrice(event.target.value)}margin="normal" id="outlined-basic" label="Price" variant="outlined" value={radio==='m'?stockPrice:price}/>
        <FormControl component="fieldset">
          <RadioGroup row aria-label="gender" name="gender1" value={radio} onChange={handleRadioChange}>
            <FormControlLabel value="m" control={<Radio color="primary"/>} label="Market" />
            <FormControlLabel value="l" control={<Radio />} label="Limit" />
          </RadioGroup>
        </FormControl>   
      </Grid>
          <Button onClick={handleSubmit} variant="contained" color="primary" style={{marginTop:8, minWidth: 270, borderRadius:5, fontSize:15}}>
            Sell
          </Button>
      </TabPanel>
  </SwipeableViews>
      
    </React.Fragment>
  );
}