def check_divisibility():

    counter = 0
    searching = True
    while searching:
        counter += 1
        potential = True
        for k in range(2, 20 + 1):
            if counter % k != 0:
                potential = False
        if potential is True:
            searching = False

    return counter


print(check_divisibility())
