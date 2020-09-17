import React,{ useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Label, ResponsiveContainer,Tooltip} from 'recharts';
import axios from 'axios';
import Skeleton from '@material-ui/lab/Skeleton';
import { Typography } from '@material-ui/core';



// Generate Sales Data


export default function Chart() {
  const [rows,setRows] = useState([]);

  useEffect(() => {
    function createData(BOS, LOM, Order_isin, aon, identifier, price, qty) {
      setRows(rows => [...rows,{ "time":'03:00', "amount":price},])
    }
    const id = setInterval(() => {
    axios.get('/orders').then(resp => {
      setRows([]);
    resp.data.map((row)=> createData(row.BOS,row.LOM,row.Order_isin,row.aon,row.identifier,row.price,row.qty))
    });}
    , 2000);
    return () => clearInterval(id);  
  }, []);
  

  return (
    <React.Fragment>
      <Typography component="h2" variant="h6" style={{color:"#ADF5FF"}} gutterBottom>
      Today
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