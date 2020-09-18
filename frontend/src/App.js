import React from 'react';
import './App.css';
import Dashboard from './components/Dashboard';
import { Switch, BrowserRouter as Router, Route } from 'react-router-dom';
import Landing from './components/Landing';
import Admin from './components/Admin';
import { createMuiTheme } from '@material-ui/core/styles';
import { ThemeProvider } from '@material-ui/styles';

const theme = createMuiTheme({
  typography: {
    fontFamily: [
      'Noto Sans',
      'Roboto',
      '"Helvetica Neue"',
      'Arial',
      'sans-serif'
    ].join(','),
  }
});

function App() {

  
  return (
    <ThemeProvider theme={theme}>
    <div className="App" >
      <Router>
        <Switch>
          <Route path="/dashboard">
            <Dashboard/>
          </Route>
          <Route path="/admin">
            <Admin/>
          </Route>
          <Route path="/">
            <Landing/>
          </Route>
        </Switch>
      </Router>
    </div>
    </ThemeProvider>
  );
}

export default App;
