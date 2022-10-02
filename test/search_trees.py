# Search trees are just lists in disguise.
# Note: this IDE automatically clears the terminal. Matlab's doesn't.

list_4_binary_search = []
input_string = input()
while input_string != "#":
    list_4_binary_search.append(input_string)
    input_string = input()

list_with_query_items = []
input_string = input()
while input_string != "#":
    list_with_query_items.append(input_string)
    input_string = input()

# The only thing different here will be the search algorithm.


def binary_search(list_w_stuff, item):
    first = 0
    last = len(list_w_stuff) - 1
    found = False   # boolean for this shit

    while first <= last and not found:
        mid = (first + last) // 2
        if list_w_stuff[mid] == item:
            found = True
        else:
            if item < list_w_stuff[mid]:
                last = mid - 1  # minus one since it's not list[mid].
            else:
                first = mid - 1

    return found


for item in list_with_query_items:
    if binary_search(list_4_binary_search, item):
        print(item + " found")
    else:
        print(item + " not found")

# Time limit exceeded. Needs to run in less than a second.
# Is a recursive call quicker? From runestone:
# binarySearch(alist[:midpoint], item)
