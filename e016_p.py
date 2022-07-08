# thnx https://stackoverflow.com/questions/46590452/power-digit-sum
# no Jayson Chacko for modulo idea!


def sum_function(number):
    sum_number = 0
    while number > 0:
        number, modulo = divmod(number, 10)     # cuts last digit every time
        sum_number += modulo   # divmod returns dividend and remainder
    return sum_number


print(sum_function(2**1000))
