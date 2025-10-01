"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 \times 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

<div class="note">HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


You're only looking for identities where:
Total digits = 9
So possible digit splits:
1-digit × 4-digit = 4-digit (1+4+4 = 9)
2-digit × 3-digit = 4-digit (2+3+4 = 9)
3-digit × 2-digit = 4-digit (3+2+4 = 9)
1-digit × 3-digit = 5-digit (1+3+5 = 9)
That greatly reduces the search space — you don't need to try every possible multiplication.
"""

from itertools import permutations

def pandigital_products() -> int:
    answer = set()
    number_perms = list(permutations([str(x) for x in range(1, 10)]))

    perms_set = sorted([str(x) for x in range(1, 10)])

    for perm in number_perms:
        first_five = perm[0:5]
        first_four = perm[0:4]
        first_prod = int(''.join(list(first_five[0:1]))) * int(''.join(list(first_five[1:])))
        second_prod = int(''.join(list(first_five[0:2]))) * int(''.join(list(first_five[2:])))
        third_prod = int(''.join(list(first_five[0:3]))) * int(''.join(list(first_five[3:])))
        fourth_prod = int(''.join(list(first_four[0:1]))) * int(''.join(list(first_four[1:])))
        
        first_set = sorted(''.join(list(first_five)) + str(first_prod))
        second_set = sorted(''.join(list(first_five)) + str(second_prod))
        third_set = sorted(''.join(list(first_five)) + str(third_prod))
        fourth_set = sorted(''.join(list(first_four)) + str(fourth_prod))

        if first_set == perms_set:
            answer.add(first_prod)
        elif second_set == perms_set:
            answer.add(second_prod)
        elif third_set == perms_set:
            answer.add(third_prod)
        elif fourth_set == perms_set:
            answer.add(fourth_prod)

    return sum(answer)





if __name__ == "__main__": 
    print(pandigital_products())