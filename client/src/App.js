import React from 'react';
import './App.css';
import Screen from './components/Screen'


function App() {

  const titleStyle = {
    fontSize: '3.5rem',
    textAlign: 'center',
    
  };
  

  return (
    
    <div className="App">
      <header className="App-header">
        <h1 style={titleStyle}>Library Noise Level</h1>
        <Screen></Screen>
      </header>

    </div>
  );
}

export default App;
