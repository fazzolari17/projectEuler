"""
Powerful Digit Counts


The $5$-digit number, $16807=7^5$, is also a fifth power. Similarly, the $9$-digit number, $134217728=8^9$, is a ninth power.
How many $n$-digit positive integers exist which are also an $n$th power?


Link to problem: https://projecteuler.net/problem=63
"""

def powerful_digit_counts(limit: int) -> int:
    count = 0
    for x in range(1, 25):
        for n in range(1, 10):
            power = n ** x
            if len(str(power)) == x:

                count += 1

    return count


if __name__ == "__main__": 
    limit = 1000
    answer = powerful_digit_counts(limit)
    print(answer)