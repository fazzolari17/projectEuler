const pythagoreanTriplet = (tripletSum) => {

  let total = 0
  let count = 1
  let a
  let b
  while(total !== tripletSum) {
    console.log(count)
    console.log('TOTAL:', total)
    a = count * count
    b = (count + 1) * (count + 1)
    let c = a + b
    total = c
    count++
  }

  return a + b
}

console.log(pythagoreanTriplet(1000))
console.log(Math.pow(3, 2))