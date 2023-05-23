let start = Date.now()

const highlyDivisibleTriangularNumber = (n) => {
  let currentTriangular = 0
  let count = 0

  while (true) {
    count = count + 1
    currentTriangular = currentTriangular + count

    let divisorCount = 0

    for (let i = 1; i < Math.sqrt(currentTriangular); i++) {
      if (currentTriangular % i === 0) {
        divisorCount = divisorCount + 2
      }
    }

    if (Number.isInteger(Math.sqrt(currentTriangular))) {
      divisorCount = divisorCount + 1
    }

    console.log(`currentTriangular is ${currentTriangular} and the divisors are ${divisorCount}`)

    if (divisorCount > n) {
      return currentTriangular
    }

  }
}

console.log(highlyDivisibleTriangularNumber(process.argv[2] || 500))


let finish = Date.now()

console.log(`took ${finish - start}ms to run`)

