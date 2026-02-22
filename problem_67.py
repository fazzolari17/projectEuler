"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are altogether! If you could check one trillion () routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

def maximum_path_sum_II(filename: str) -> int:
    triangle = list()
    with open(filename, 'r') as file:
        for line in file:
            triangle.append([int(x) for x in line.strip().split(' ')])

    for row in range(len(triangle)-2, -1, -1):
        for column in range(len(triangle[row])):
            triangle[row][column] += max(triangle[row + 1][column], triangle[row + 1][column + 1])
    return triangle[0][0]
if __name__ == "__main__": 
    filename = "problem_67_test_file.txt"
    print(maximum_path_sum_II(filename))