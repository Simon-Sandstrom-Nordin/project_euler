class LinkedQ:

    def __init__(self):
        self.__first = None
        self.__last = None

    # Creates the first node if the queue is empty, adds a new node at the end if not
    def enqueue(self, data):
        if self.is_empty():
            self.__first = Node(data, None)
            self.__last = self.__first
        else:
            self.__last.next = Node(data, None)
            self.__last = self.__last.next

    # Returns the data from the first then sets the node after the first first
    def dequeue(self):
        data = self.__first.data
        self.__first = self.__first.next
        return data

    # Loops through queue until it reaches the last node (where next is None)
    def size(self):
        node = self.__first
        size = 0
        while node is not None:
            node = node.next
            size = size + 1

        return size

    # Returns emptiness of queue
    def is_empty(self):
        return self.__first is None

    # Peek method
    def peek(self):
        try:
            return self.__first.data
        except AttributeError:  # If next node is None
            return None


class Node:

    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node
