file = open("e013_.txt", "r")

number = 0
for line in file:
    line_integer = int(line.strip("\n"))
    print(line_integer)
    number += line_integer

file.close()

print(number)
