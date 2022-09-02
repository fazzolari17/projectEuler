const theSumSquareDifference = n => {
  const sumOfTheSquares = num => {
    let total = 0
    for (let i = 1; i <= num; i++) {
      total += i * i
    }
    return total
  }
  
  const squareOfTheSums = num => {
    let total = 0
    for (let i = 1; i <= num; i++) {
      total += i 
    }
    total = total * total
    return total
  }

  return squareOfTheSums(n) - sumOfTheSquares(n)
}
  console.log(theSumSquareDifference(100))