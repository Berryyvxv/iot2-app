import React from 'react';
import './App.css';
import Screen from './components/Screen'
import Table from './components/Table'

function App() {
  const titleStyle = {
    fontSize: '3.5rem',
    textAlign: 'center',
    fontFamily: 'Nova Square, Poppins, sans-serif', // Use Nova Square and Poppins with light 300 weight
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
