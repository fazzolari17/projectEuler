var sieveOfErathosthenes = require('sieve-of-eratosthenes')
const primes = sieveOfErathosthenes(2000000)

const summationOfPrimes = () => {

  return primes.reduce((acc, val) => acc + val, 0)
}

console.log(summationOfPrimes())
