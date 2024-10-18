import React from 'react'
import { FaBars } from "react-icons/fa";

const navbar = () => {
  return (
    <div className='navbar'>
      <div className='logo'>
         <img src='https://zerodha.com/static/images/logo.svg'></img>
      </div>
      <div className='links'>
          <li><a href=''>SignUp</a></li>
          <li><a href=''>About</a></li>
          <li><a href=''>Products</a></li>
          <li><a href=''>Pricing</a></li>
          <li><a href=''>Support</a></li>
          <FaBars  className='bar-icon'/>

      </div>
    </div>
  )
}

export default navbar