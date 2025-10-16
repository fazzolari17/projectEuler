"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""
import math

def pandigital_prime(n: int) -> (int, int):
    pandigitals = list()
    def is_prime(n: int) -> bool:
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0 and i != n:
                return False
        return True

    def is_pandigital(n: int) -> bool:
        reference = sorted(list(range(1, (len(str(n)))+1)))
        return reference == sorted([int(x) for x in str(n)])


    for i in range(1, n+1):
        if is_prime(i):
            if '0' in str(i):
                continue
            if is_pandigital(i):
                pandigitals.append((i, len(str(i))))
                print(f"{i} is prime and pandigital")

    return max(pandigitals)
if __name__ == "__main__": 

    limit = 7999999
    answer = pandigital_prime(limit)
    print(f"Answer is {answer[0]} and has {answer[1]} digits")
    