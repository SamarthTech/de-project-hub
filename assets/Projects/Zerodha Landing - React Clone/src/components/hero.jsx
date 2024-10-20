import React from 'react'
import Landing from '../assets/images/Landing.png'

const hero = () => {
  return (
    <div className='hero'>
      <div className='hero-img-box'>
        <img src={Landing} alt="Landing" className='landing-img' />
      </div>
      <div className='hero-text-box'>
        <h1>Invest in everything</h1>
        <p>Online platform to invest in stocks, derivatives, mutual funds, ETFs, bonds, and more.</p>
      </div>
      <div className='hero-btn-box'>
        <button className='hero-btn'>Sign Up For Free</button>
      </div>
    </div>
  )
}

export default hero