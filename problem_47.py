"""
The first two consecutive numbers to have two distinct prime factors are:
    14 = 2 X 7
    15 = 3 X 5
The first three consecutive numbers to have three distinct prime factors are:
    644 = 2**2 X 7 X 23 
    645 = 3 X 5 X 43
    646 = 2 X 17 X 19
Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""
from math import sqrt

def find_prime_factors(n):
    factors = set()
    # Check for 2 as a factor seperately to optimize loop
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    # Check for odd factors
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)

    return factors

def distinct_prime_factors():
    consecutive_count = 0
    current_number = 2
    while True:
        factors = find_prime_factors(current_number)
        if len(factors) == length:
            consecutive_count += 1
            if consecutive_count == length:
                return current_number - length + 1
        else:
            consecutive_count = 0
        current_number += 1
        if current_number > limit:
            return None


        
        
if __name__ == '__main__':
    print(distinct_prime_factors())