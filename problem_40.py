"""
An irrational decimal fraction is created by concatenating the positive integers:
0.12345678910[1]112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If n represents the nth digit of the fractional part, find the value of the following expression.
1 * 10 * 100 * 1000 * 10000 * 100000 * 1000000
"""
import math

def champernownes_constant(n: int) -> list:
    """
        Although unneeded I chose to not put the numbers in a string or array and index into the positions. The string or list would 
        not have been prohibitively long, but with larger numbers it could have been, so I chose to just keep track of the current 
        number and index and extract that number as to not put the large list into memory, brcause I thought that is what is was asking
        me to do in the beginning of this exercise.
    """
    
    positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
    result = []
    count = 0
    for n in range(1, n+1):
        length = len(str(n))
        for a in range(1, length+1):
            if count + a in positions:
                result.append((count + a, str(n)[a-1]))


        count += length

    return result


if __name__ == "__main__": 
    answer = champernownes_constant(1000000)
    print(math.prod([int(x[1]) for x in answer]))