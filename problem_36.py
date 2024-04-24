def is_palindrome(n):
    if n == int(str(n)[::-1]):
        return True
    return False

def double_base_palindromes(limit):
    palindrome_numbers = []
    for i in range(1, limit):
        base_ten = i 
        binary = int(bin(i)[2:])
        if is_palindrome(base_ten) and is_palindrome(binary):
            palindrome_numbers.append(i)
    return sum(palindrome_numbers) 

if __name__ == '__main__':
    print(double_base_palindromes(1000000))