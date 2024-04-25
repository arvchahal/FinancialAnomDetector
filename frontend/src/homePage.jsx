import React from 'react';
import {Link} from 'react-router-dom';
import './homePage.css'
import Main from './main'
const homePage = () =>{
  return (
    <div>
      <div>
        <Main/>
      <div className="header">
        <h1>Get an up to date financial anomaly detector of 200,000+ stocks</h1>
        <p>Utilizing market features such as RSI, MACD, EMA, and more to get the most accurate results</p>
        <Link to="/app" className="get-started">Get started</Link>
      </div>


 
    </div>
    </div>



  );

};
export default homePage;
