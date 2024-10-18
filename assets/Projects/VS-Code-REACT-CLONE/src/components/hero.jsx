import React from 'react'
import HeroImage from '../assets/images/heroVSCode.png'
const hero = () => {
  return (
    <div className='hero'>
     <div className='hero-texts'>
      <h1>
      Code faster with AI
      </h1>
      <p>
      Visual Studio Code with GitHub Copilot supercharges your
      </p>
      <p>
      code with AI-powered suggestions, right in your editor.
      </p>
     </div>
     <div className='btn-hero'>
      <button className='btn-hero-1'>Download for Windows</button>
      <button className='btn-hero-2'>Try Github Copilot</button>
     </div>
     <div className='hero-image'>
      <img src={HeroImage} alt='No Image is Found'></img>
     </div>

    </div>
  )
}

export default hero