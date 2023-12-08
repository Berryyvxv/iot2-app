import React, {useState, useEffect} from 'react';
import './App.css';
import Screen from './components/Screen'
import Table from './components/Table'

function App() {
  const [data, setData] = useState ([{}])
  // data is the actual varible, and setData used to manipulate the state of these data varible

useEffect(() => { 
  fetch("/noiseLevel").then(
    res => res.json()
  ).then(
    data => {
      setData(data)
      console.log(data)
    }
  )
}, [])


  const titleStyle = {
    fontSize: '3.5rem',
    textAlign: 'center',
    
  };
  

  return (
    
    <div className="App">
      <header className="App-header">
        <h1 style={titleStyle}>Library Noise Level</h1>
        {(typeof data.noiseLevel === 'undefined') ? (
          <p> Loading ...</p>
        ): (
          data.noiseLevel.map((noiseLevel, i) => (
            <p key={i}>{noiseLevel}</p>
          ))
        )
        
        }

        <Screen></Screen>
      </header>

    </div>
  );
}

export default App;
