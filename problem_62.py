"""
Cubic Permutations

The cube, 41063625 345^3, can be permuted to produce two other cubes: 56623104 384^3 and 66430125 405^3. In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube.

Link to problem: https://projecteuler.net/problem=62
"""


def cubic_permutations(desired_perms: int) -> list:
    answers = dict()
    i = 2
    while True:
        cube = ''.join(sorted(str(i**3)))

        if cube in answers:
            answers[cube].append(i**3)
        else:
            answers[cube] = [i**3]
        if len(answers[cube]) == desired_perms:
            return answers[cube] 


        i+=1

if __name__ == "__main__": 
    desired_perms = 3
    answer = cubic_permutations(desired_perms)
    print(f"smallest cube for which exactly five permutations of its digits are cube is {min(answer)}")
