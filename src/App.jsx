import './App.css'
import "./index.css"
import { useState } from "react";

function App() {
  const [totalClasses, setTotalClasses] = useState("");
  const [attendedClasses, setAttendedClasses] = useState("");
  const [requiredPercentage, setRequiredPercentage] = useState("");

  const [calculated, setCalculated] = useState(false);
  const [attendance, setAttendance] = useState(0);
  const [status, setStatus] = useState("");
  const [canMiss, setCanMiss] = useState(0);

  const handleCalculate = () => {
    const T = Number(totalClasses);
    const A = Number(attendedClasses);
    const R = Number(requiredPercentage);

    //basic validation 
    if (T <= 0 || A < 0 || R <= 0 || A > T){
      alert("Please enter valid numbers.");
      return;
    }

    //currnt attendance %
    const currentAttendance = (A / T) * 100; 
    setAttendance(currentAttendance.toFixed(2));

    //status
    if (currentAttendance >= R) {
      setStatus("SAFE");
    } else {
      setStatus("DANGER");
    }

    //max classes you can miss
    const maxMiss = Math.floor((A*100) / R - T);
    setCanMiss(maxMiss > 0 ? maxMiss : 0);

    setCalculated(true);
  };

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

        <button className='calculate-btn' onClick={handleCalculate}>
          Calculate
        </button>


        <div className='divider' />

        {!calculated && (
          <p className='placeholder'>
            Enter your details and click calculate
          </p>
        )}

        {calculated && (
          <div className='results'>
            <h2 className='big-number'>{attendance}%</h2>
            <p className={`status ${status.toLowerCase()}`}>
              {status === "SAFE" ? "SAFE " : "DANGER "}
            </p>

            <p className='miss-text'>
              You can miss <strong>{canMiss}</strong> classes
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App
