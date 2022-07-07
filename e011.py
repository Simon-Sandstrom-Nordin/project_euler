file = open("e011.txt", "r")
dictionary = {}
line_counter = 0
for line in file:
    line_list = line.strip("\n").split(" ")
    index = 1
    line_counter += 1
    for number in line_list:
        dictionary[str(line_counter) + ":" + str(index)] = int(number)
        index += 1
file.close()

horizontal_products = []
for l_c in range(1, 20 + 1):
    for ind in range(1, 20 + 1 - 3):
        product = dictionary[str(l_c) + ":" + str(ind)] * dictionary[str(l_c) + ":" + str(ind + 1)] \
                * dictionary[str(l_c) + ":" + str(ind + 2)] * dictionary[str(l_c) + ":" + str(ind + 3)]
        horizontal_products.append(product)

vertical_products = []
for l_c in range(1, 20 + 1 - 3):
    for ind in range(1, 20 + 1):
        product = dictionary[str(l_c) + ":" + str(ind)] * dictionary[str(l_c + 1) + ":" + str(ind)] \
                * dictionary[str(l_c + 2) + ":" + str(ind)] * dictionary[str(l_c + 3) + ":" + str(ind)]
        vertical_products.append(product)

right_diagonal_products = []
for l_c in range(1, 20 + 1 - 3):
    for ind in range(1, 20 + 1 - 3):
        product = dictionary[str(l_c) + ":" + str(ind)] * dictionary[str(l_c + 1) + ":" + str(ind + 1)] \
                * dictionary[str(l_c + 2) + ":" + str(ind + 2)] * dictionary[str(l_c + 3) + ":" + str(ind + 3)]
        right_diagonal_products.append(product)

left_diagonal_products = []
for l_c in range(1, 20 + 1 - 3):
    for ind in range(4, 20 + 1):
        product = dictionary[str(l_c) + ":" + str(ind)] * dictionary[str(l_c + 1) + ":" + str(ind - 1)] \
                * dictionary[str(l_c + 2) + ":" + str(ind - 2)] * dictionary[str(l_c + 3) + ":" + str(ind - 3)]
        left_diagonal_products.append(product)

all_products = horizontal_products + vertical_products + right_diagonal_products + left_diagonal_products

print("maximum is:", max(all_products))
