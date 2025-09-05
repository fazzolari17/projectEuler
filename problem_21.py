"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a 
e b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.  
"""


def amicable_numbers(n):
    solution = []
    result = []
    for i in range(1, n):
        first_nums = []
        second_nums = []
        for j in range(1, i):
            if i % j == 0:
                first_nums.append(j)
        first_total = sum(first_nums)
        for k in range(1, first_total):
            if first_total % k == 0:
                second_nums.append(k)
        
        if sum(second_nums) == i:
            solution.append((first_total, sum(second_nums)))
    return sum([t[0] for t in solution if t[0] != t[1]])


if __name__ == "__main__": 
    # Expected Result 31626
    print(amicable_numbers(10000)) 