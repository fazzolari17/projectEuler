def find_multiples(n):
    multiples = []
    for i in range(2, 7):
        multiples.append(n * i)
    multiples = [int(''.join(sorted(str(n)))) for n in multiples]
    return multiples

def is_a_permutation(data: list):

    for i in range(len(data)):
        if data[i] != data[0]:
            return False
    return True

def permuted_multiples():
    for i in range(1, 1000000):
        multiples = find_multiples(i)
        if is_a_permutation(multiples):
            return i

if __name__ == '__main__':
    print(permuted_multiples())