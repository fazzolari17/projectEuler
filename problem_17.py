def number_letter_counts(limit: int):
    number_dict = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 
    19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'one hundred', 
    200: 'two hundred', 300: 'three hundred', 400: 'four hundred', 
    500: 'five hundred', 600: 'six hundred', 700: 'seven hundred', 
    800: 'eight hundred', 900: 'nine hundred', 1000: 'one thousand'
}
    count = 0
    for n in range(1, limit):
        if len(str(n)) == 1:
            count += len(number_dict[n])
        if len(str(n)) == 2:
            if n < 21:
                count += len(number_dict[n])
            # accounts for the numbers that have a zero as a unit 
            elif n % 10 == 0:
                count += len(number_dict[n])
            else:
                tens = (n // 10) * 10
                units = n % 10
                count += len(f"{number_dict[tens]} {number_dict[units]}".replace(" ", ""))
        if len(str(n)) == 3:
            quo, re = divmod(n, 100)
            # if the number is exactly 100 or 200 etc
            if n % 100 == 0:
                count += len(number_dict[n].replace(" ", ""))
            elif re % 10 == 0:
                quotient, remainder = divmod(n, 100)
                hundreds = quotient * 100
                tens = (remainder // 10) * 10
                count += len(f"{number_dict[hundreds]} and {number_dict[tens]}".replace(" ", ""))
            else:
                quotient, remainder = divmod(n, 100)
                hundreds = quotient * 100
                tens = (remainder // 10) * 10
                if tens == 0:
                    units = n % 10
                    print(hundreds, tens, units)
                    count += len(f"{number_dict[hundreds]} and {number_dict[units]}".replace(" ", ""))
                elif re < 21:
                    count += len(f"{number_dict[hundreds]} and {number_dict[re]}".replace(" ", ""))
                else:
                    units = n % 10
                    count += len(f"{number_dict[hundreds]} and {number_dict[tens]} {number_dict[units]}".replace(" ", ""))
        if len(str(n)) == 4:
            count += len(number_dict[n].replace(" ", ""))
    return count

print(number_letter_counts(1001))
# print('Check:', len('web dev web'.replace(" ", "")))

# def test(number: int):
#     # hundreds = (number // 100) * 100
#     quotient, remainder = divmod(n, 100)
#     hundreds = quotient * 100
#     tens = (remainder // 10) * 10
#     units = n % 10
#     print(hundreds, tens, units)
# test(342)