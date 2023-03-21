const powerDigitSum = () => {
  const result = BigInt(Math.pow(2, 1000))
  const arr = result.toString().split('').map(Number)
  let sum = 0

  for (let i = 0; i < arr.length; i++) {
    sum += arr[i]
  }

  return sum
}

console.log(powerDigitSum())