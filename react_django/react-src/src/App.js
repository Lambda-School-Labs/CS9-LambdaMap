import HPsettings from './components/settings/HP-settings/HPsettings';
import JSprofile from './components/jobseeker-profile/JSprofile';
import React, { Component } from 'react';
import { Route } from 'react-router-dom';
import './App.css';
import SignUp from './components/landing/signUp';
require('dotenv').config();
// import SignIn from './components/landing/signIn';

// import { Provider } from 'react-redux';

class App extends Component {
 
  render() {
    return (
      <div className="App">
          <Route exact path="/" component={JSprofile} />
          <Route path="/settings" component={HPsettings} />
          <Route path="/register" component={SignUp} />
      </div>
    );
  }
}

export default App;



// class App extends Component {
//   render() {
//     return (
//       <div>
//         <SignIn />
// {/* ======= */}
{/* // import HPnav from './components/nav/company/HPnav'*/}