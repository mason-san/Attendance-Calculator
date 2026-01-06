import './App.css'
import "./index.css"
import { useState } from "react";

function App() {
  const [totalClasses, setTotalClasses] = useState("");
  const [attendedClasses, setAttendedClasses] = useState("");
  const [requiredPercentage, setRequiredPercentage] = useState("");

  return (
    <div className='app'>
      <div className='title'>Attendance Calculator</div>

      <div className='card'>
        <label>Total Number of classes</label>
        <input 
          type='number'
          value={totalClasses}
          onChange={(e) => setTotalClasses(e.target.value)}
          />

        <label>Classes attended</label>
        <input
          type='number'
          value={attendedClasses}
          onChange={(e) => setAttendedClasses(e.target.value)}
          />

        
        <label>Required Classes</label>
        <input  
          type='number'
          value={requiredPercentage}
          onChange={(e) => setRequiredPercentage(e.target.value)}
          />

        <button className='calculate-btn'>Calculate</button>

        <div className='divider' />
        <p className='placeholder'>
          Enter your details and click calculate
        </p>
      </div>
    </div>
  );
}

export default App
