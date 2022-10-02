# Trollkarlen
# Input: String of symbols separated by a space.
# Output: Row of cards as wizard would put them out

# LinkedQ might be a good option here.

class Queue:
    def __init__(self):
        self.items = []     # They got a list!

    def is_empty(self):
        return self.items == []     # No semicolon! This is python.

    def enqueue(self, item):
        self.items.insert(0, item)  # shoves from front

    def dequeue(self):
        return self.items.pop()     # pops (returns) the last element away

    def size(self):
        return len(self.items)


q = Queue()
hand_string = input()
hand_list = hand_string.split(" ")
# print(hand_list)
# this is just to check it worked. It did.
for card in hand_list:
    q.enqueue(card)
# end
# we don't do that here. Only in Matlab, Julia, and shit
# print(q.size())
# Seems to work.

output_list = []
while q.is_empty() is False:
    # q.enqueue(q.dequeue())  # does this work? Order of operations and shit?
    # ... maybe not. :(
    card = q.dequeue()
    q.enqueue(card)
    output_list.append(q.dequeue())

# disp()
# We don't do that here, go back to MATLAB. Go home, disp().

print(*output_list)
