import { useState } from 'react'
import Register from './components/Register'
import Login from './components/Login'
import './App.css'

function App() {
  const [response, setResponse] = useState(null)

  return (
    <>
      <h1>React + Django</h1>
      <hr />
      <Register setResponse={setResponse} />
      <hr />
      <Login setResponse={setResponse} />

      <p>Token: {response?.token}</p>
    </>
  )
}

export default App
