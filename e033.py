# Digit cancelling fractions

def digit_checker(a, b):
    if a < 10 or b < 10 or a > 100 or b > 100:
        return None
    if a % 10 == 0 and b % 10 == 0:
        return None
    fraction = a / b
    if fraction > 1 or fraction == 1:
        return None

    a_one = a % 10
    a_ten = (a - a_one) // 10
    b_one = b % 10
    b_ten = (b - b_one) // 10

    if a_one == a_ten and b_one == b_ten:   # divisible by 11, trivial
        return None

    if b_one != 0:
        fraction_one_one = a_one / b_one
        fraction_ten_one = a_ten / b_one
    else:
        fraction_one_one = 0
        fraction_ten_one = 0
    if b_ten != 0:
        fraction_one_ten = a_one / b_ten
        fraction_ten_ten = a_ten / b_ten
    else:
        fraction_one_ten = 0
        fraction_ten_ten = 0

    if a_ten == b_ten:
        if fraction == fraction_one_one:
            return str(a) + "/" + str(b) + " = " + str(a_one) + "/" + str(b_one)
    if a_one == b_ten:
        if fraction == fraction_ten_one:
            return str(a) + "/" + str(b) + " = " + str(a_ten) + "/" + str(b_one)
    if a_ten == b_one:
        if fraction == fraction_one_ten:
            return str(a) + "/" + str(b) + " = " + str(a_one) + "/" + str(b_ten)

    if a_one == b_one:
        if fraction == fraction_ten_ten:
            return str(a) + "/" + str(b) + " = " + str(a_ten) + "/" + str(b_ten)


for a in range(10, 100):
    for b in range(10, 100):
        result = digit_checker(a, b)
        if result is not None:
            print(result)
