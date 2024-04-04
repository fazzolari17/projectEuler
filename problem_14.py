# const start = Date.now()

# const longestCollatzSequence = (limit) => {
#   let startingNumber = 1
#   let longestSequence = 1
#   // let startingNumberOfLongest

#   while (startingNumber < limit) {
#     startingNumber = startingNumber - 1

#     let count = 0

#     for (let i = startingNumber; i > 1;) {
#       if (startingNumber % i === 0) {
#         i = i / 2
#         count = count + 1
#       } else if (startingNumber % i === 1) {
#         i = i * 3 + 1
#         count = count + 1
#       }
#       console.log(count)
#     }

#     if (count > longestCollatzSequence) {
#       longestSequence = count
#       startingNumberOfLongest = startingNumber
#     }
#   }
#   return { longestSequence, startingNumberOfLongest }

# }

# console.log(longestCollatzSequence())

# const finish = Date.now()

# console.log(`The function took ${(finish - start) / 1000} Seconds to run`)


def longest_collatz_sequence(starting_number):
    seq = (0, [])
    count = starting_number
    # print('starting number', count)
    while count > 1:
        temp_seq = []
        n = count
        temp_seq.append(n)
        while n > 1:
            # print('N', n)
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1

            temp_seq.append(n)

        if len(temp_seq) > len(seq[1]):
            seq = (count, temp_seq)

        count -= 1
    
    return seq
number, sequence = longest_collatz_sequence(999999)
print(number, len(sequence))