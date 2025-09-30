"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""

import math 

def is_prime(n: int) -> bool:
    if n == 1:
        return False

    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and i != n:
            return False
    return True


def truncatable_primes(n):
    primes = []
    for number in range(8, n):
        if is_prime(number):
            truncated_nums = [number]
            num = [int(x) for x in str(number)]
            # Run the left to right truncation 
            for i in range(1, len(num)):
                new_num = num[i:]
                truncated_nums.append(int(''.join([str(x) for x in new_num])))
            # Run the right to left truncation 
            for i in range(len(num)-1, 0, -1):
                new_num = num[:i]
                truncated_nums.append(int(''.join([str(x) for x in new_num])))

            for i in range(len(truncated_nums)):
                if is_prime(truncated_nums[i]) == False:
                    break
                elif i == len(truncated_nums) - 1:
                    primes.append(number)
    return primes

if __name__ == "__main__": 
    print(sum(truncatable_primes(1000000)))
