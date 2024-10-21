import React from 'react'
import VSCode from '../assets/images/VS Code.png'
import { MdOutlineDarkMode } from "react-icons/md";
import { CiSearch } from "react-icons/ci";

const navbar = () => {
  return (
    <div className='navbar'>
      <div className='navbar-left'>
        <img src={VSCode} alt='No Image Found'></img>
        <a href=''>Visual Studio Code</a>
        <li><a href=''>Docs</a></li>
        <li><a href=''>Updates</a></li>
        <li><a href=''>Blog</a></li>
        <li><a href=''>API</a></li>
        <li><a href=''>Extensions</a></li>
        <li><a href=''>FAQ</a></li>
        <li><a href=''>Github Copilot</a></li>
      </div>
      <div className='navbar-right'>
        <MdOutlineDarkMode  className='dark-icon'/>

    
        <div class="group">
          <svg class="icon" aria-hidden="true" viewBox="0 0 24 24"><g><path d="M21.53 20.47l-3.66-3.66C19.195 15.24 20 13.214 20 11c0-4.97-4.03-9-9-9s-9 4.03-9 9 4.03 9 9 9c2.215 0 4.24-.804 5.808-2.13l3.66 3.66c.147.146.34.22.53.22s.385-.073.53-.22c.295-.293.295-.767.002-1.06zM3.5 11c0-4.135 3.365-7.5 7.5-7.5s7.5 3.365 7.5 7.5-3.365 7.5-7.5 7.5-7.5-3.365-7.5-7.5z"></path></g></svg>
          <input placeholder="Search Docs" type="search" class="input"></input>
        </div>

        <div className='navbar-btn'>
          <button className='btn-1'>Download</button>
        </div>
    
      </div>
    </div>
  )
}

export default navbar