import React from 'react';
import './App.css';
import Screen from './components/Screen'
import image from "./image/Figma.png"; 



function App() {

  const titleStyle = {
    fontSize: '3.5rem',
    textAlign: 'center',
    
  };
  const titleStyle2 = {
    fontSize: '1.2rem',
    textAlign: 'center',
    
  };

  return (

    <div className="App">
      <header className="App-header" style={{ backgroundImage:`url(${image})` }}>
      {/* <div style={{ backgroundImage:`url(${image})` }}>
        
        </div> */}
        <h1 style={titleStyle}>Library Noise Level</h1>
        <p style={titleStyle2}>
    This app facilitates Librarian's mission via identifying table ID's & detecting the warning types,
    <br />
    Also, it checks if the tables are available or have people sitting.
</p>


        <Screen></Screen>
      </header>

    </div>
  );
}

export default App;
