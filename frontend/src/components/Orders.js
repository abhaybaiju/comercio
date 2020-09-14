import React, { useEffect, useState } from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from './Title';
import axios from 'axios';
import Skeleton from '@material-ui/lab/Skeleton';

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
    function createData(BOS, LOM, Order_isin, aon, identifier, price, qty) {
      setRows(rows => [{ "BOS":BOS, "LOM":LOM, "Order_isin":Order_isin, "aon":aon, "identifier":identifier, "price":price, "qty":qty}, ...rows,])
    }
    const id = setInterval(() => {
    axios.get('/orders').then(resp => {
    setRows([]);
    resp.data.map((row)=> createData(row.BOS,row.LOM,row.Order_isin,row.aon,row.identifier,row.price,row.qty))
    console.log("Fetching",resp.data); 
    });}
    , 1000);
    return () => clearInterval(id);  
  }, []);
  
  
  console.log("ROWS",rows)
  const classes = useStyles();
  return (
    
    <React.Fragment>
      <Title>Recent Trades</Title>
      {rows!== [] ? (
      <Table size="medium">
        <TableHead>
          <TableRow>
            <TableCell>ISIN</TableCell>
            <TableCell>Identifier</TableCell>
            <TableCell>Type</TableCell>
            <TableCell>Quantity</TableCell>
            <TableCell align="right">Sale Price</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.slice(0,5).map((row) => (
            <TableRow key={row.identifier}>
              <TableCell>{row.Order_isin}</TableCell>
              <TableCell>{row.identifier}</TableCell>
              <TableCell>{row.BOS}</TableCell>
              <TableCell>{row.qty}</TableCell>
              <TableCell align="right">{row.price}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>) : (<Skeleton variant="rect" />)}
      <div className={classes.seeMore}>
        <Link color="primary" href="#" onClick={preventDefault}>
          See more orders
        </Link>
      </div>
    </React.Fragment>
  );
}