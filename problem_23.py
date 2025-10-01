"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def get_divisors_sum(n: int) -> int:
    """Return sum of proper divisors of n."""
    total = 1  # 1 is always a divisor (except for n=1)
    sqrt_n = int(n ** 0.5)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total if n > 1 else 0

def is_abundant(n: int) -> bool:
    return get_divisors_sum(n) > n


def non_abundant_sums(limit: int) -> int:
    """Find the sum of all positive integers which cannot be written
    as the sum of two abundant numbers."""
    # Step 1: get all abundant numbers up to limit

    abundants = [i for i in range(12, limit+1) if is_abundant(i)]

    # Step 2: mark sums of two abundant numbers
    can_be_written = [False] * (limit+1)
    print(can_be_written)
    for i in range(len(abundants)):
        for j in range(len(abundants)):
            s = abundants[i] + abundants[j]
            if  s <= limit:
                can_be_written[s] = True
            else:
                break

    return sum(i for i in range(1, limit + 1) if not can_be_written[i])
    # abundant_nums = []
    # sums_of_abundant = []

    # for i in range(1, limit):
    #     temp_divs = []
    #     for j in range(1, i):
    #         if i % j == 0:
    #             temp_divs.append(j)

    #     total_of_divs = sum(temp_divs)
    #     if total_of_divs > i:
    #         abundant_nums.append(i)
        
    # totaled = [sum([n, m]) for n in abundant_nums for m in abundant_nums]
    # abundant_nums = set(abundant_nums)
    # non_abundant_sums = set(totaled)
    # return sum(list(abundant_nums.difference(non_abundant_sums)))
                



if __name__ == "__main__": 
    print(non_abundant_sums(28123))
    # print(non_abundant_sums(100))