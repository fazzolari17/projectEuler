def digit_fibonacci():
    count = 2
    a = 1
    b = 1
    c = 0

    while len(str(c)) < 1000:
        c = a + b
        a = b 
        b = c 
        count += 1

    return count

if __name__ == '__main__':
    print(digit_fibonacci())

