import math, datetime
start_time = datetime.datetime.now()
def prime_numbers(length):
    def is_prime(n: int):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0 and i != n:
                return False
        return True

    prime = []
    count = 2
    while len(prime) < length:
        if is_prime(count):
            prime.append(count)
        count += 1
    return prime

if __name__ == '__main__':  
    prime_numbers = prime_numbers(10001)
    for n in prime_numbers:
        print(n)
    end_time = datetime.datetime.now()
    print((end_time - start_time))