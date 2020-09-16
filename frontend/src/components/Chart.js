import React,{ useEffect, useState } from 'react';
import { useTheme } from '@material-ui/core/styles';
import { LineChart, Line, XAxis, YAxis, Label, ResponsiveContainer,Tooltip} from 'recharts';
import Title from './Title';
import axios from 'axios';
import Skeleton from '@material-ui/lab/Skeleton';



// Generate Sales Data


export default function Chart() {
  const theme = useTheme();

  const [rows,setRows] = useState([]);

  useEffect(() => {
    function createData(BOS, LOM, Order_isin, aon, identifier, price, qty) {
      setRows(rows => [{ "time":'03:00', "amount":price}, ...rows,])
    }
    const id = setInterval(() => {
    axios.get('/orders').then(resp => {
      
    resp.data.map((row)=> createData(row.BOS,row.LOM,row.Order_isin,row.aon,row.identifier,row.price,row.qty))
    console.log("Fetching chart",resp.data); 
    });}
    , 2000);
    return () => clearInterval(id);  
  }, []);
  
  
  console.log("Chart ROWS",rows)


  return (
    <React.Fragment>
      <Title>Today</Title>
      <ResponsiveContainer>
        {rows.length>0 ? (
        <LineChart
          data={rows}
          margin={{
            top: 16,
            right: 16,
            bottom: 0,
            left: 24,
          }}
        >
          <YAxis stroke={theme.palette.text.secondary}>
            <Label
              angle={270}
              position="left"
              style={{ textAnchor: 'middle', fill: theme.palette.text.primary }}
            >
              Price ($)
            </Label>
          </YAxis>
          <Line type="monotone" dataKey="amount" stroke={theme.palette.primary.main} dot={true} />
          <Tooltip/>
        </LineChart>) : (<Skeleton variant="rect" animation="wave"/>)}
      </ResponsiveContainer>
    </React.Fragment>
  );
}