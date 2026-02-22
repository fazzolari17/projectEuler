"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,
$$\begin{align}
&amp;44 -> 32 -> 13 -> 10 -> 1 -> 1
&amp;85 -> \mathbf{89} -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
\end{align}$$

Therefore any chain that arrives at  or  will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at  or .

How many starting numbers below ten million will arrive at ?
Link: https://projecteuler.net/problem=92
"""

def square_digit_chains(limit: int) -> int:
    count = 0

    for number in range(1, limit+1, 1):
        print(number)
        chain = number
        while True:

            n = str(chain)
            n = [n for n in n]
        
            chain = 0
            for digit in n:
                chain += int(digit)**2

            if chain == 89:
                count += 1 
                break 
            elif chain == 1:
                break 

    return count


if __name__ == "__main__": 
    limit = 10000000
    print(square_digit_chains(limit))