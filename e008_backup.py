number_string = ""

file = open('e008.txt', 'r')
for line in file:
    number_string += line.strip("\n")
number_integer = int(number_string)
# print(number_string)
# print(numer_integer)
# print(len(number_string))
file.close()

max_product = 0

for k in range(0, len(number_string) - 12):
    product = int(number_string[k]) * int(number_string[k+1]) * int(number_string[k+2]) * int(number_string[k+3]) * int(number_string[k+4]) * int(number_string[k+5]) * int(number_string[k+6]) * int(number_string[k+7]) * int(number_string[k+8]) * int(number_string[k+9]) * int(number_string[k + 10]) * int(number_string[k+11]) * int(number_string[k + 12])

    if product > max_product:
        max_product = product

print(max_product)
