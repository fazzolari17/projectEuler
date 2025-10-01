"""
Euler discovered the remarkable quadratic formula:
n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. The product of the coefficients, -79 and 1601, is -126479.
Considering quadratics of the form:

n^2 + an + b, where |a| &lt; 1000 and |b| <= 1000
where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

import math

def is_prime(n: int) -> bool:
    if n == 1:
        False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and i != n:
            return False
    return True

def quadratic_primes():
    longest = 0
    coefficients = None
    A = [x for x in range(-999, 1000)]
    B = [x for x in range(-1000, 1001)]

    for a in A:
        for b in B:
            n = 0
            while True:
                ans = (n**2) + (a*n) + b

                if is_prime(abs(int(ans))) == False:
                    break
                if n > longest:
                    longest = n
                    coefficients = (a, b)

                n += 1
                
    

    return (coefficients, longest)
if __name__ == "__main__": 
    coefficients, longest = quadratic_primes()

    print(f"Coefficients: {coefficients} Product: {coefficients[0] * coefficients[1]} Longest: {longest}")