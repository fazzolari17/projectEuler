
const largestPrimeFactor = num => {
  let factor = 2
  while (num !== factor) {
    if (num % factor === 0) {
      num = num / factor
    } else {
      factor ++
    }
  }
  return factor
}

console.log(largestPrimeFactor(600851475143))