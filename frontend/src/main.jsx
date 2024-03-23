import React from 'react'
import stock from './components/stock.mp4'

const main = () =>{
  return (
    <div className='main'>
      <video src={stock} autoPlay loop muted/>


    </div>


  ); 
};
export default main