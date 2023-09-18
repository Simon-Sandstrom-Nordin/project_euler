def binary_search(the_list, key):
    left = 0
    right = len(the_list)

    while left <= right:
        middle = (left + right) // 2
        item = the_list[middle]
        if item == key:
            return item
        else:
            if key < item:
                right = middle - 1
            else:
                left = middle + 1

    return None
    # return the_list[left] if the_list[left] == key else None


def main():
    # Läs in listan
    indata = input().strip()
    the_list = indata.split()
    # Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()


main()
