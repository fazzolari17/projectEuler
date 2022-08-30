const evenFibonacciNum = () => {
  let a = 0
  let b = 1
  let c = 0
  let sum = c

  while (c <= 4000000) {
    c = a + b
    a = b
    b = c
    if (c % 2 === 0) {
      sum += c
    }
  }

  return sum

}

console.log(evenFibonacciNum(33))