"""
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation,   5 3 = 10.
In general,   n r = \dfrac{n!}{r!(n-r)!}, where r <= n, n! = n * (n-1) * ... * 3 * 2 * 1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: {23} {10} = 1144066.
How many, not necessarily distinct, values of n r for 1 <= n <= 100, are greater than one-million?
"""

import math

def factorial(n: int) -> int:
    total = n
    for i in range(n-1, 0, -1):
        total *= i
    return total if total != 0 else 1


def combinatoric_selections(limit: int) -> int:
    """
    I chose to solve this with my own factorial function rather than use the math.factorial just because I wanted to write the function myself.
    I could have just used math.factorial to get the same result, with same or similar running time. 
    The fastest calcs are done using math.comb(n, r) and I sought this out when I thought the problem wanted range of 1000 because it was taking 
    to long to compute.
    """
    total = list()
    for n in range(1, limit+1):
        for r in range(1, n+1):
            # result = math.comb(n, r)
            result = factorial(n) / (factorial(r) * factorial(n-r))
            # result = math.factorial(n) / (math.factorial(r) * math.factorial(n-r))
            if result > 1000000:

                total.append((n,r))

    return len(total)
    

if __name__ == "__main__": 
    print(combinatoric_selections(100))
