import { useState } from "react"
import { login } from "../handleRequests"

function Login({ setResponse }) {
  const [formData, setFormData] = useState({
    username: '',
    password: ''
  })

  const loginUrl = "http://127.0.0.1:8000/api/auth/login/"

  async function handleSubmit(e) {
    e.preventDefault()
    const data = await login(loginUrl, formData)
    setResponse(data)
    console.log(data)
  }

  const handleChange = (e) => {
    setFormData(data => ({ ...data, [e.target.name]: e.target.value }))
  }

  return (
    <form method="post" onSubmit={handleSubmit}>
      <div>
        <label>Username</label>
        <br />
        <input type="text" name="username" value={formData.username} onChange={handleChange} />
      </div>

      <div>
        <label>Password</label>
        <br />
        <input type="password" name="password" value={formData.password} onChange={handleChange} />
      </div>

      <button type="submit">Login</button>
    </form>
  )
}

export default Login