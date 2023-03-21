const pythagoreanTriplet = (range) => {
  let a = 0
  let b = 0
  let c = 0

  for (let i = 0; i < range; i++) {
    for(let j = i+1; j < range; j++) {
      a = i
      b = j
      c = Math.sqrt((a * a) + (b * b))
      if((a + b + c) === 1000) {
        if((a * b * c) === 0) continue

        return a * b * c
      }
    }
  }
}
console.log(pythagoreanTriplet(376))