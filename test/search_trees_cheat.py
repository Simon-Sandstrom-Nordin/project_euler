# Input: list of strings (?).

# Cheatzy method: screw search trees (even tho the time
# complexity is O(log(n)) {binary log}. Do linear search, O(n).
# time complexity thing: n/(2^i) = 1 <=> n = 2^i.
# This is width-first? Then solve for i = blog(n).
# anyway...
list_4_linear_search = []
input_string = input()
while input_string != "#":
    list_4_linear_search.append(input_string)
    input_string = input()
print(list_4_linear_search)

list_with_query_items = []
input_string = input()
while input_string != "#":
    list_with_query_items.append(input_string)
    input_string = input()
print(list_with_query_items)

for item in list_with_query_items:
    if item in list_4_linear_search:
        print(item + " found")
    else:
        print(item + " not found")

# wait, does python do linear search with "in"? I don't know this.
