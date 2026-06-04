import { useState } from "react"
import { register } from "../handleRequests"

function Register({ setResponse }) {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    password2: ''
  })

  const registerUrl = "http://127.0.0.1:8000/api/auth/register/"

  async function handleSubmit(e) {
    e.preventDefault()
    const data = await register(registerUrl, formData)
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
        <label>Email</label>
        <br />
        <input type="email" name="email" value={formData.email} onChange={handleChange} />
      </div>

      <div>
        <label>Password</label>
        <br />
        <input type="password" name="password" value={formData.password} onChange={handleChange} />
      </div>

      <div>
        <label>Repeat Password</label>
        <br />
        <input type="password" name="password2" value={formData.password2} onChange={handleChange} />
      </div>

      <button type="submit">Register</button>
    </form>
  )
}

export default Register