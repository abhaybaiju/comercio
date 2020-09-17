import React,{ useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Label, ResponsiveContainer,Tooltip} from 'recharts';
import axios from 'axios';
import Skeleton from '@material-ui/lab/Skeleton';
import { Typography } from '@material-ui/core';
import { useStateValue } from '../StateProvider'; 


// Generate Sales Data


export default function Chart() {
  const [rows,setRows] = useState([]);
  const [{ user, stockPrice }, dispatch] = useStateValue();
  useEffect(() => {
    function createData(price) {
      setRows(rows => [...rows,{ "time":'03:00', "amount":price},])
    }
    setRows([]);
    const id = setInterval(() => {
    axios.get('/securities').then(resp => {
      resp = resp.data.filter(function(item){
        return item.name === securities[user];         
    })
    dispatch({
      type: 'SET_PRICE',
      stockPrice: resp[0].ltprice,
  });
    createData(resp[0].ltprice);
    });}
    , 2000);
    return () => clearInterval(id);  
  }, [user]);

  const securities = ['Apple','Microsoft','IBM','Xerox', 'Pixar'];

  return (
    <React.Fragment>
      <Typography component="h2" variant="h6" style={{color:"#ADF5FF"}} gutterBottom>
      {securities[user]}
    </Typography>
      <ResponsiveContainer >
        {rows.length>0 ? (
        <LineChart
          data={rows}
          margin={{
            top: 16,
            right: 16,
            bottom: 16,
            left: 2,
          }}
        >
          <YAxis stroke="#ADF5FF" margin/>
          <Line strokeWidth={4} isAnimationActive={true} animationEasing='ease-in-out' type="monotone" dot={false} dataKey="amount" stroke="#ADF5FF" />
        </LineChart>) : (<Skeleton variant="rect" animation="wave"/>)}
      </ResponsiveContainer>
    </React.Fragment>
  );
}