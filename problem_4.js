const multiplyNumbers = number => {
  let i = 0
  let sum = 0
  let largest = 0
  while (i < number) {
    for (let j = 0; j < number; j++) {
      sum = i * j

      if (reverseSum(sum)) {
        if(sum > largest) {
          largest = sum
        }
      }

    }

    i++
  }

  return largest
}

const reverseSum = sum => {
  let result = sum.toString().split('').reverse().join('')

  if (sum == result) {
    return true
  }

}
console.log(multiplyNumbers(1000))