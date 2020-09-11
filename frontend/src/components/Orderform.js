import React from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import SwipeableViews from 'react-swipeable-views';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import {Tabs, Tab, Grid, Button} from '@material-ui/core';
import Title from './Title';

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
  const classes = useStyles();

  const [value, setValue] = React.useState(0);

  const handleTabChange = (event, newValue) => {
    setValue(newValue);
  };

  const handleChangeIndex = (index) => {
    setValue(index);
  };

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
      <Grid >
        <TextField margin="normal" id="outlined-basic" label="Quantity" variant="outlined" />
        <TextField margin="normal" id="outlined-basic" label="Price" variant="outlined" />      
          </Grid>
          <Button variant="contained" color="primary">
            Place Order
          </Button>
      </TabPanel>
      <TabPanel value = {value} index={1}>
      <Grid >
        <TextField margin="normal" id="outlined-basic" label="Quantity" variant="outlined" />
        <TextField margin="normal" id="outlined-basic" label="Price" variant="outlined" />
          </Grid>
          <Button variant="contained" color="primary">
            Place Order
          </Button>
      </TabPanel>
  </SwipeableViews>
      
    </React.Fragment>
  );
}