import math, time

"""
Prime Pair Sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

Link to Problem: https://projecteuler.net/problem=60
"""


def is_prime(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0 and i != n:
            return False
    return True

def concat_is_prime(a: int, b: int) -> bool:
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))

def run_checks(prime_pairs: list, n: int) -> bool or list:
    if n in prime_pairs:
        return False
    else:
        for number in prime_pairs:
            if concat_is_prime(number, n) == False:
                return False

    prime_pairs.append(n)
    return prime_pairs

def add_number(prime_pairs: list, primes: list) -> set or bool: 
    for n in primes:
        if n in prime_pairs:
            continue
        result = run_checks(prime_pairs, n)
        if result != False:
            return result
    return False

def prime_pair_sets():
    lowest = 10000000000
    generated_primes = [p for p in range(2, 10000) if is_prime(p)]
    primes = set()

    for a in range(len(generated_primes)):
        x = [generated_primes[a]]
        while True:
            new_list = add_number(x, generated_primes)
            if new_list:
                if len(new_list) == 5:
                    return new_list
                if tuple(new_list) in primes:
                    break 
                else:
                    primes.add(tuple(new_list))
                x = new_list
            else:
                break
            
    return primes
if __name__ == "__main__": 
    start_time = time.time()
    answer = prime_pair_sets()
    print(f"The Tuple is: {answer} and the Total is: {sum(answer)}")
    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time:.4f} seconds")
