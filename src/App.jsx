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

  const [needAttend, setNeedAttend] = useState(0);

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

    const minRequiredAttended = (R * T) / 100;

    if (A >= minRequiredAttended) {
      setStatus("SAFE");
      const maxMiss = Math.floor(T - A - (minRequiredAttended - A));
      setCanMiss(maxMiss > 0 ? maxMiss: 0);
      setNeedAttend(0);
    } else {
      setStatus("DANGER");
      setCanMiss(0);

      const needed = Math.ceil(minRequiredAttended - A);
      setNeedAttend(needed > 0 ? needed: 0);
    }

    setCalculated(true);
  };

  return (
    <div className='app'>
      <div className='title'>Attendance Calculator</div>

      <div className='card'>
        <label>Total classes in the semester (for this subject)</label>
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

            {status ===  "SAFE" && (
              <p className='miss-text'>
                You can miss <strong>{canMiss}</strong> classes
              </p>
            )}

            {status === "DANGER" && (
              <p className='miss-text'>
                You need to attend <strong>{needAttend}</strong> classes to recover
              </p>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App
