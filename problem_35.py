import math
def circle_prime(n):
    number_str = str(n)
    rotations = set()

    for i in range(len(number_str)):
        rotated_number = int(number_str[i:] + number_str[:i])
        rotations.add(rotated_number)

    for number in rotations:
        if not is_prime(number):
            return False
    return True

def is_prime(n: int):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0 and i != n:
                return False
        return True

def circular_primes(limit):
    count = 0
    for n in  range(2, limit):
        if is_prime(n):
            if circle_prime(n):    
                count += 1
    return count



if __name__ == '__main__':
    print(circular_primes(1000000))