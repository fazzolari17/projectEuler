"""
Large Non-Mersenne Prime

The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form $2^{6972593} - 1$; it contains exactly $2\,098\,960$ digits. Subsequently other Mersenne primes, of the form $2^p - 1$, have been found which contain more digits.
However, in 2004 there was found a massive non-Mersenne prime which contains $2\,357\,207$ digits: $28433 \times 2^{7830457} + 1$.
Find the last ten digits of this prime number.
Link to problem: https://projecteuler.net/problem=97
"""


def large_non_mersenne_prime():
    # The complexity with this problem is the very large number that is generated from the equation 28433 * 2^7830457 + 1. This number 
    # can be easily handled with python but the problem comes from trying to access the last ten digits, python has issues turning numbers
    # into very larges strings. In order to solve this problem after the number is generated use the modulus % 10**10 will give you the last 
    # ten digits this can be altered by changing the last number such that when you want 12 digits 10**12 would provide that.
    return (28433 * (2**7830457) + 1) % 10**10 


    # return r_2 % 10**12

if __name__ == "__main__": 
    print(large_non_mersenne_prime())