async function register(url, data) {
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })

    const resData = await response.json()

    return resData
  } catch (error) {
    console.error("Error: ", error)
  }
}

async function login(url, data) {
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })

    const resData = await response.json()

    return resData
  } catch (error) {
    console.error("Error: ", error)
  }
}

export { register, login }