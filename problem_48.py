"""
Self Powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def self_powers(n: int) -> int:
    total = 0
    for i in range(1, n+1):
        total += i**i
    return str(total)

if __name__ == "__main__": 

    print(self_powers(1000)[-10:])