const find10001stPrime = () => {
  let primes = [1, 2]
  let multiples = []

  let count = 2
  while(primes.length < 10001)
    count++
  for(let i = count; i < 100000000; i++) {
    if(i % count === 0) {
      multiples.push(i)
    }
  }
  return primes
}

console.log(find10001stPrime())