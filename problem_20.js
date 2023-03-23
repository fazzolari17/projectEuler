const factorialDigitSum = (factorial) => {
  let total = BigInt(factorial)
  for (let i = factorial - 1; i >= 1; i--) {
    total = (total * BigInt(i))
  }
  total = Array.from(String(total), Number)
  return total.reduce((a, b) => a + b, 0)
}

console.log(factorialDigitSum(100))