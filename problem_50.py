import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0 and i != n:
            return False
    return True

def list_of_primes(limit):
    primes = set()
    
    for i in range(2, limit):
        if is_prime(i):
            primes.add(i)

    return sorted(primes)

def consectuve_primes(limit):
    primes = list_of_primes(limit)
    count = 0
    terms = []

    while count < len(primes):
        temp_term = []

        for i in range(count, len(primes)):
            temp_term = primes[count:i]
            
            if sum(temp_term) > limit:
                break

            if sum(temp_term) < limit and is_prime(sum(temp_term)):
                if len(temp_term) > len(terms):
                    terms = temp_term

        count += 1

    return sum(terms)

if __name__ == '__main__':
    print(consectuve_primes(1000000))