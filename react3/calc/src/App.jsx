import { useState } from 'react';
import './App.css'
import { Screen } from './components/Screen'
import { Numpad } from './components/Numpad';

function App() {
  const [buffer, setBuffer] = useState("1234");

  const addToBuffer = newChar => {
    setBuffer(buffer + newChar);
  }

  return (
    <div id='calc' className='border'>
      <Screen display={buffer} />
      <Numpad />
    </div>
  )
}

export default App
