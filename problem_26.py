"""
A unit fraction contains $1$ in the numerator. The decimal representation of the unit fractions with denominators $2$ to $10$ are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.1(66666), and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
import pprint
p = pprint.pprint

def reciprocal_cycles(n: int):
    longest = ''
    answer = None
    for number in range(1, n):
        for power in range(1, 1000):
            # The following line reduces the time the calculations take due to the elimnation of all values 
            # that are divisible by 2 and 5 as they will terminate and will not generate repeating cycles
            if number % 2 == 0 or number % 5 == 0: 
                break
                
            num = 10**power
            quotient, remainder = divmod(num, number)
            
            if remainder == 1:
                if len(str(quotient)) > len(longest):
                    longest = str(quotient)
                    answer = number
                break

    return longest, answer

if __name__ == "__main__": 
    limit = 1000
    repeating_sequence, number = reciprocal_cycles(10000)
    print(f"{number} creates the longest recurring cycle in numbers under d < {limit}")
