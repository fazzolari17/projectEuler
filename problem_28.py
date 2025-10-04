def number_spiral_diagonals(size: int):
    total = 1
    for n in range(3, size + 1, 2):
        corner_one = n**2
        corner_two = corner_one - (n - 1)
        corner_three = corner_two - (n - 1)
        corner_four = corner_three - (n - 1)
        total += corner_one + corner_two + corner_three + corner_four

    return total
if __name__ == "__main__": 
    answer = number_spiral_diagonals(1001)

    print(f"The sum of the numbers on the diagonal are {answer}")