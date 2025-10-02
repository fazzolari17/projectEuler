"""
A googol (10^{100}) is a massive number: one followed by one-hundred zeros; 100^{100} is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""

def powerful_digit_sum(n: int) -> int:
    largest = None
    for a in range(1, n+1):
        for b in range(1, n+1):
            total = a**b
            digital_num = sum([int(x) for x in str(int(total))])
            if largest is None or digital_num > largest:
                largest = digital_num

    return largest

if __name__ == "__main__": 
    limit = 100
    result = powerful_digit_sum(limit)
    print(f"The largest digital sum of a^b in a range of {limit}\n  Result: {result}")
