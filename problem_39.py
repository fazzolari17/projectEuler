"""
Integer Right Triangles

If p is the perimeter of a right angle triangle with integral length sides, {a, b, c}, there are exactly three solutions for p = 120.
    {20,48,52}, {24,45,51}, {30,40,50}
For which value of p le 1000, is the number of solutions maximised?
"""
import math, pprint

def integer_right_triangles(p: int) -> (int, int):
    permiter_list = dict()
    for a in range(1, p+1):
        for b in range(a+1, p+1):
            for c in range(b+1, p+1):
                if a+b+c > p:
                    continue
                if a**2 + b**2 == c**2:
                    # print(f"{a}^2 + {b}^2 = {c}^2")
                    # print(f"{a**2 + b**2} = {c**2}")
                    if a+b+c in permiter_list:
                        permiter_list[a+b+c].append((a,b,c))
                    else:
                        permiter_list[a+b+c] = [(a,b,c)]

    
    longest = (0, 0)
    for key, value in permiter_list.items():

        if len(value) > longest[1]:
            longest = (key, len(value))

    return longest
if __name__ == "__main__": 
    limit = 1000
    p, solutions = integer_right_triangles(limit)
    print(f"For which value of p <= {limit}, is the number of solutions maximised?")
    print(f"p = {p} and the number of solutions is {solutions} for p <= {limit}")
    