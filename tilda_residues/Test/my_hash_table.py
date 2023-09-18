class Node:
    def __init__(self, key="", data=None, next=None):
        self.key = key
        self.data = data
        self.next = next


class Hashtable:

    def __init__(self, size):
        self.size = size
        self.slots = [None] * size
        self.n_elements = 0

    def store(self, key, data):
        key_hash = self.hashfunction(key)
        node = self.__search_node(key)
        if node is None:
            self.slots[key_hash] = Node(key, data)
            self.n_elements += 1

        elif node.key == key:
            node.data = data
            return

        elif node.next is None:
            node.next = Node(key, data)
            self.n_elements += 1

    # collision resolution is though collision lists
    def __search_node(self, key):
        key_hash = self.hashfunction(key)
        if self.slots[key_hash] is not None:
            node = self.slots[key_hash]
            if node.key == key:
                return node
            next = node.next
            while next is not None:
                node = next
                if node.key == key:
                    return node
                next = node.next
            return node
        else:
            return None

    def search(self, key):
        node = self.__search_node(key)
        if node is not None and node.key == key:
            return node.data
        raise KeyError

    def hashfunction(self, key):
        if key is None:
            return 0
        my_hash = 0
        bit_shift_num = 0
        for char in key:
            my_hash += ord(char)
            bit_shift_num = ord(char)
        # bit shift to increase size of small numbers to assure uniform distribution
        my_hash = my_hash << bit_shift_num
        return my_hash % self.size

    def get_load_factor(self):
        return self.n_elements / self.size

    def get_max_collisions(self):
        counter = 0
        index = 0
        while index < self.size:
            temp_counter = 0
            if self.slots[index] is None:
                pass
            else:
                current_node = self.slots[index]
                while current_node is not None:
                    temp_counter += 1
                    current_node = current_node.next
            if temp_counter > counter:
                counter = temp_counter
            index += 1
        return counter

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        try:
            _ = self.search(key)
            return True
        except KeyError:
            return False
