"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

import math

def is_prime(n: int) -> bool:
        if n == 1:
            return False

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0 and i != n:
                return False

        return True

def generate_primes(n: int) -> list:
    primes = list()

    for i in range(10000, n):
        if is_prime(i):
            primes.append(i)
    return primes

def prime_digit_replacements(length: int) -> (int, list):
    primes = generate_primes(1000000)

    for prime in primes:
        nums = set([int(x) for x in str(prime)])
        for num in nums:
            family = []
            for n in range(0, 10):
                new_number = int(str(prime).replace(str(num), str(n)))
                if is_prime(new_number) and len(str(new_number)) == len(str(prime)):
                    family.append(new_number)
                    # print(f"Number: {new_number} Is Prime: {is_prime(new_number)}")
            if len(family) == length:
                return (prime, family)


if __name__ == "__main__": 
    length_of_prime_value_family = 8
    prime, family = prime_digit_replacements(length_of_prime_value_family)
    print(f'First prime family that contains {length_of_prime_value_family} primes')
    print(f"  Prime Number: {prime}\n  Family: {family}")

    # print(is_prime(121313))