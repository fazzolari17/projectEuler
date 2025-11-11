
import math 

def largest_exponential(filename: str) -> int:
    biggest = 0
    index = 0

    with open(filename, 'r') as file:

        for i, line in enumerate(file, start=1):
            base, exp = map(int, line.strip('\n').split(','))
            r = exp * math.log(base)
            print(biggest, i)
            if r > biggest:
                biggest = r
                index = i
    return index

if __name__ == "__main__": 
    answer = largest_exponential('base_exp.txt')
    print(answer)