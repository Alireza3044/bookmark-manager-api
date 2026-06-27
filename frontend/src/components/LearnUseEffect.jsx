import { useEffect, useState } from "react"

function LearnUseEffect() {
  const [randomNum, setRandomNum] = useState(0)

  useEffect(() => {
    console.log("Random Number Generated");
  }, [randomNum])

  const generateRandomNum = () => {
    const num = Math.floor(Math.random() * 100)
    setRandomNum(num)
  }
  return (
    <>
      <h1>Random Number: {randomNum}</h1>
      <button onClick={generateRandomNum}>Generate Random Number</button>
    </>
  )
}

export default LearnUseEffect