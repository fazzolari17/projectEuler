"""
Goldbach's Other Conjecture

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import math

def goldbachs_other_conjecture(limit: int) -> list:
    def is_odd(n: int) -> bool:
        return n % 2 != 0

    def is_prime(n: int) -> bool:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0 and i != n:
                return False

        return True
    odd_composites = []
    primes = []
    for n in range(2, limit+1):
        if is_prime(n):
            primes.append(n)
        if is_odd(n) and not is_prime(n):
            odd_composites.append(n)

    def it_satisifies_conjecture(composite: int, primes: list) -> bool:
        for prime in primes:
            if prime > composite:
                break
            for square in range(1, 100):
                if prime + 2 * (square**2) == composite:
                    # print(f'{composite} = {prime} + 2 x {square}^2')
                    return True
        
        return False

    for composite in odd_composites:
        if it_satisifies_conjecture(composite, primes) != True:
            return composite
            
    # return odd_composites[:100], primes[:100]
if __name__ == "__main__": 
    composite  = goldbachs_other_conjecture(1000000)

    print(composite)
