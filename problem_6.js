// const theSumSquareDifference = n => {
//   const sumOfTheSquares = num => {
//     let total = 0
//     for (let i = 1; i <= num; i++) {
//       total += i * i
//     }
//     return total
//   }

//   const squareOfTheSums = num => {
//     let total = 0
//     for (let i = 1; i <= num; i++) {
//       total += i
//     }
//     total = total * total
//     return total
//   }

//   return squareOfTheSums(n) - sumOfTheSquares(n)
// }

// console.log(theSumSquareDifference(100))



const isPrime = num => {
  for(let i = 2, s = Math.sqrt(num); i <= s; i++)
    if(num % i === 0) return false
  return num > 1
}

const arrayOfNumbers = num => {
  const array = []
  for (let i = 0; i < num; i++) {
    array.push(i)
  }
  return array
}

console.log(arrayOfNumbers(1000000))

