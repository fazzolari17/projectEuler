"""
Spiral Primes

Starting with $1$ and spiralling anticlockwise in the following way, a square spiral with side length $7$ is formed.
31
38 <span class="red">17 16 15 14 13 30
39 18 <span class="red"> 5  4 <span class="red"> 3 12 29
40 19  6  1  2 11 28
41 20 <span class="red"> 7  8  9 10 27
42 21 22 23 24 25 26<span class="red">43 44 45 46 47 48 49
It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that $8$ out of the $13$ numbers lying along both diagonals are prime; that is, a ratio of $8/13 \approx 62\%$.
If one complete new layer is wrapped around the spiral above, a square spiral with side length $9$ will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below $10\%$?

Link to problem https://projecteuler.net/problem=58
"""
import math 

def spiral_primes() -> int:
    def is_prime(n: int) -> bool:
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0 and i != n:
                return False
        return True
    

    primes = []
    non_primes = [1]
    n = 3
    while True:
        corner_one = n**2
        corner_two = corner_one - (n - 1)
        corner_three = corner_two - (n - 1)
        corner_four = corner_three - (n - 1)
        corners = [corner_one, corner_two, corner_three, corner_four]
        for corner in corners:
            if is_prime(corner):
                primes.append(corner)
            else:
                non_primes.append(corner)
        if len(primes) > 1 and len(non_primes) > 1:
            
            if math.ceil((len(primes) / (len(non_primes) + len(primes))) * 100) <= 10:
                return n


        n += 2
if __name__ == "__main__": 
    answer = spiral_primes()
    print(answer)