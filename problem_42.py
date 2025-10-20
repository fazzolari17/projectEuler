"""
Coded Triangle Numbers

The ...n...<sup>th</sup> term of the sequence of triangle numbers is given by, ...t_n = \frac12n(n+1)...; so the first ten triangle numbers are:
......1, 3, 6, 10, 15, 21, 28, 36, 45, 55, .........
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is ...19 + 11 + 25 = 55 = t_{10}.... If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
import string

def coded_triangel_numbers():
    letters = string.ascii_uppercase

    triangle_numbers = [1]
    count = 0

    for n in range(2, 1001):
        triangle_numbers.append(triangle_numbers[-1] + n)

    with open("words.txt", "r") as file:
        for line in file:
            words = line.split(",")
            for word in words:
                word = word.replace('"', '')
                x = 0
                for letter in word:
                    index = letters.index(letter) + 1
                    x += index

                if x in triangle_numbers:
                    count += 1


    return count
if __name__ == "__main__": 
    answer = coded_triangel_numbers()
    print(f"There are {answer} triangle words in word.txt file")