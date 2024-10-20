import { useState } from 'react'
import './App.css'

function App() {
  const [ color , setColour] = useState("olive")

  return (
    <div className = " w-full h-screen duration-200" style= {{backgroundColor: color}}> 
    <h1 className='text-white text-5xl flex justify-center text-justify'>Rohit Kumar Kundu</h1>
      <div className="fixed flex-wrap justify-center bottom-12 inset-x-0 px-2">
       
        <div className="flex flex-wrap justify-center gap-3 shadow-lg bg-white px-3 py-2 rounded-3xl ">
              <button onClick={() => setColour("red")}   className="outline-none px-4 py-1 rounded-full text-white shado-lg" style={{backgroundColor: "red"}} > Red</button>
              <button onClick={() => setColour("gray")}  className="outline-none px-4 py-1 rounded-full text-white shado-lg" style={{backgroundColor: "gray"}} > Gray </button> 
              <button onClick={() => setColour("green")} className="outline-none px-4 py-1 rounded-full text-white shado-lg" style={{backgroundColor: "green"}} > Green</button>
              <button onClick={() => setColour("black")} className="outline-none px-4 py-1 rounded-full text-white shado-lg" style={{backgroundColor: "black"}} > Black</button>
              <button onClick={() => setColour("blue")}  className="outline-none px-4 py-1 rounded-full text-white shado-lg" style={{backgroundColor: "blue"}} > Blue</button>
        </div>

      </div>
   </div>
  )
}

export default App
