const start = Date.now()

function smallestMultiple(n) {
  let largest = n
  let unsolved = true
  let i
  while (unsolved) {
    for (i = 2; i < n; i++) {
      if (largest % i !== 0) {
        largest = largest + n
        break
      }
    }
    if (i === n) {
      unsolved = false
      return largest
    }
  }
  return largest
}

console.log(smallestMultiple(20))

const end = Date.now()
console.log(`${end - start}MS`)

// console.log(smallestMult(20))