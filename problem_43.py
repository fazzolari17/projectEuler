"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:
d_2d_3d_4=406 is divisible by 2
d_3d_4d_5=063 is divisible by 3
d_4d_5d_6=635 is divisible by 5
d_5d_6d_7=357 is divisible by 7
d_6d_7d_8=572 is divisible by 11
d_7d_8d_9=728 is divisible by 13
d_8d_9d_{10}=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import itertools

def generate_pandigital(length: int) -> list:
    pandigital_list = list(itertools.permutations(range(length)))

    return pandigital_list
    
def sub_string_divisibility():
    pandigital_list = generate_pandigital(10)

    result = list()
    for item in pandigital_list:
        primes = [0, 2, 3, 5, 7, 11, 13, 17]
        for index in range(1, len(item)-2):
            n = int(''.join([str(x) for x in item[index:index+3] if str(x) not in '(), ']))
            
            if n % primes[index] == 0:
                if index == len(item)-3:
                    result.append(item)
            else:
                break
    
    numbers_result = []
    for item in result:
        new_item = ''
        item = str(item)
        for l in item:
            if l not in "(), ":
                new_item += l
        numbers_result.append(int(new_item))
    return numbers_result



if __name__ == "__main__": 
    answer = sub_string_divisibility()
    print(f"{answer} is the list of 0-9 pandigital numbers that match the criteria.")
    print(f"{sum(answer)} is the sum of those numbers.")
