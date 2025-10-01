"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations

def nth_permutation(nums, n):
    perms = []
    for p in permutations(sorted(nums)):
        perms.append(p)
    
    return ''.join([str(x) for x in perms[n+1]])


if __name__ == "__main__": 
    print(nth_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000))
    # print(nth_permutation([0, 1, 2,], 1000000))