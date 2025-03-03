import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

const baseUrl = import.meta.env.VITE_BACKEND_URL

interface UserModel{
  id : number
  name : string
}

function App() {
  const [count, setCount] = useState<number | undefined>(undefined)
  const [user,setUser] = useState<UserModel[]>([])
  
  useEffect(() => {
    fetch(`${baseUrl}/count`, {
    }).then((value) => {
      value.json().then((value)=>{
        setCount(value.count)
      })
    })
    fetch(`${baseUrl}/users`, {
    }).then((value) => {
      value.json().then((value)=>{
        setUser(value)
      })
    })
  }, [])
  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => {
          fetch(`${baseUrl}/count`, {
            method: "POST"
          }).then((value) => {
            value.json().then((value)=>{
              setCount(value.count)
            })
            
            
          })
        }}>
          count is {count}
        </button>
        
        {
          user.map((value)=>(
            <div style={{
              backgroundColor : "grey",
              marginBottom : "2px",
              borderRadius : "5px",
              width : "100%"
            }}>
              {value.name}
            </div>
          ))
        }
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
