import React from 'react';
import './App.css';
import Dashboard from './components/Dashboard';
import { Switch, BrowserRouter as Router, Route } from 'react-router-dom';
import Landing from './components/Landing';
function App() {

  
  return (
    <div className="App" >
      <Router>
        <Switch>
          <Route path="/dashboard">
            <Dashboard/>
          </Route>
          <Route path="/">
            <Landing/>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
