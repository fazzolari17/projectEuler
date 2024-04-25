"""
 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 45.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
def factorial(n):
    if n == 0:
        return 1
    total = n
    while n > 1:
        total *= n - 1
        n = n - 1
    return total

def digit_factorials(limit):
    total = 0
    for i in range(3, 1000000):
        numbers = [item for item in str(i)]
        factorials = [factorial(int(n)) for n in numbers]
        if sum(factorials) == i:
            total += i
    return total


if __name__ == '__main__':
    print(digit_factorials(5000000))    
    