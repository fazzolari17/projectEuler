"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
 (i) each of the three terms are prime, 
 and, 
 (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?

"""
import math
from itertools import permutations

def is_prime(n: int):
    '''
    Used to check if a number is prime.
    '''
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and i != n:
            return False
    return True

def find_arithmetic_nums(l: list):
    '''
    This function finds the arithmetic permutations, by using c = 2b - a.
    '''
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            ans = 2*l[j] - l[i]
            if ans in l:
                return (l[i], l[j], ans) 
    return False

def prime_permutations(n):
    answer = []
    primes = []
    for number in range(1000, n):
        if is_prime(number):
            num = [int(n) for n in str(number)]
            perm_list = []
            for perm in list(permutations(num)):
                if len(str(int(''.join(str(x) for x in perm)))) == 4:
                    perm_list.append(int(''.join(str(x) for x in perm)))


            perm_list = list(set(filter(is_prime, perm_list))) # Filter the prime numbers from the permutations
            primes.append(perm_list)

            for item in primes:
                # Filters the permutations that are three digits such that 1063 can be 0163 so that only 4 digit remain
                if len(item) < 3:
                    continue
                else:
                    if find_arithmetic_nums(item) != False:
                        answer.append(find_arithmetic_nums(item))


    return set(answer) # Returned as a set to remove duplicates




if __name__ == "__main__": 
    first, second = prime_permutations(10000)

    print(f"First: {first} Total: {sum(first)} Concatenated: {''.join(str(x) for x in first)}")
    print(f"Second: {second} Total: {sum(second)} Concatenated: {''.join(str(x) for x in second)}")

    # print(find_arithmetic_nums([1487, 1847, 4817, 4871, 7481, 7841, 8147, 8741]))
    # for item in [1487, 1847, 4817, 4871, 7481, 7841, 8147, 8741]:
    #     print(f"Number: {item} - is_prime = {is_prime(item)}")





























# import math 
# from itertools import permutations

# def is_prime(n):
#     for i in range(2, int(math.sqrt(n) + 1)):
#         if n % i == 0 and i != n:
#             return False
#     return True
# def find_common_difference(primes: list):
#     differences = {}
#     for i in range(len(primes)):
#         for j in range(i, len(primes)):
#             difference = primes[j] - primes[i] 
#             if i in differences:
#                 differences[i].append(difference)
#             else:
#                 differences[i] = []
#                 differences[i].append(difference)

#         # arithmetric_sequence_differences
#     for i in range(len(differences)):
#         for j in range(i + 1, len(differences)):
#             if differences[i] * 2 == differences[j]:
#                 print('equal', differences[j])
#     print(differences)

# def find_permutations(n):
#     number = str(n)
#     perm = permutations(str(n))
#     perms = [''.join(perm) for perm in perm]
#     prime_permutations = []
#     for number in perms:
#         if is_prime(int(number)):
#             prime_permutations.append(int(number))

#     print(prime_permutations)
#     print(find_common_difference(sorted(prime_permutations)))
#     # for i in range(len(number)):
#     #     number = number[i:] + number[:i]
#     #     permutations.append(number)
#     # permutations = sorted(permutations)
#     # print(permutations)
#     # prime_permutations = []
#     # for n in permutations:
#     #     if is_prime(int(n)):
#     #         prime_permutations.append(int(n))
#     # return prime_permutations

# def prime_permutations():

#     for i in range(1000, 10000):
#         pass
#         # permutations = find_permutations(i)

    
# if __name__ == '__main__':
#     print(prime_permutations())
#     print(find_permutations(1487))
#     print(is_prime(8714))
#     print(is_prime(7148))