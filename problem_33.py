"""
Digit Cancelling Fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""

def digit_cancelling_fractions():
    numerator_product = 1
    denominator_product = 1
    for top in range(10, 100):
        for bottom in range(top+1, 100):
            if top % 10 == 0 and bottom % 10 == 0:
                continue
            else:
                first_num, second_num = str(top)
                first_den, second_den = str(bottom)
                if second_num == first_den:
                    reduced_top = int(first_num)
                    reduced_bottom = int(second_den)
                    if reduced_top != 0 and reduced_bottom != 0 and reduced_top/reduced_bottom < 1:
                        if top/bottom == reduced_top/reduced_bottom:
                            numerator_product *= reduced_top
                            denominator_product *= reduced_bottom

    return numerator_product, denominator_product

if __name__ == "__main__": 
    numerator, denominator = digit_cancelling_fractions()
    print(f"{int(numerator/8)}/{int(denominator/8)}")