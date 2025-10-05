"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

"""

def coin_sums(target: int):
    """
        Unfortunately I was having prblems understanding the solution to this problem this is the solution and it works, but 
        I do not fully understand it and will have to revisit to try to understand the problem.
    """
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]

    return ways[target]



if __name__ == "__main__": 
    print(coin_sums(200))