import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from './Title';
import axios from 'axios';
import Skeleton from '@material-ui/lab/Skeleton';
import { Button } from '@material-ui/core';

// Generate Order Data
function preventDefault(event) {
  event.preventDefault();
}

const useStyles = makeStyles((theme) => ({
  seeMore: {
    marginTop: theme.spacing(3),
  },
}));



export default function Orders() {
  const [rows,setRows] = useState([]);

  useEffect(() => {
    function createData(id, BOS, LOM, ISIN, aon, identifier, price, qty) {
      setRows(rows => [{ "id":id,"BOS":BOS, "LOM":LOM, "ISIN":ISIN, "aon":aon, "identifier":identifier, "price":price, "qty":qty}, ...rows,])
    }
    const id = setInterval(() => {
    axios.get('/Manualorders').then(resp => {
    setRows([]);
    resp.data.map((row)=> createData(row.id,row.BOS,row.LOM,row.ISIN,row.aon,row.identifier,row.price,row.qty))
    });}
    , 2000);
    return () => clearInterval(id);  
  }, []);
  
  
  const classes = useStyles();
  return (
    
    <React.Fragment>
      <Title>Manual Orders</Title>
      {rows.length>0 ? (
      <Table size="medium">
        <TableHead>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell>ISIN</TableCell>
            <TableCell>Type</TableCell>
            <TableCell>Type(LOM)</TableCell>
            <TableCell>Quantity</TableCell>
            <TableCell align="right">Price</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.slice(0,5).map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.id}</TableCell>
              <TableCell>{row.ISIN}</TableCell>
              <TableCell>{row.BOS==='b'?"Buy":"Sell"}</TableCell>
              <TableCell>{row.LOM==='l'?"Limit":"Market"}</TableCell>
              <TableCell>{row.qty}</TableCell>
              <TableCell align="right">{row.price}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>) : (<Skeleton animation="wave" variant="rect" height={300}/>)}
      <div className={classes.seeMore}>
        <Button variant="outlined" color="primary" href="/admin" >
          See all orders
        </Button>
      </div>
    </React.Fragment>
  );
}