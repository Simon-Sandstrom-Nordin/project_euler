# I hate programming. I mean I love it. It's like factorio.
# Pokémon
class Pokemon:

    def __init__(self,
                 number,
                 Name,
                 Type1,
                 Type2,
                 Total,
                 HP,
                 Attack,
                 Defense,
                 SpAtk,
                 SpDef,
                 Speed,
                 Generation,
                 Legendary):
        self.Number = int(number)
        self.Name = str(Name)
        self.Type1 = str(Type1)
        self.Type2 = str(Type2)
        self.Total = int(Total)
        self.HP = int(HP)
        self.Attack = int(Attack)
        self.Defense = int(Defense)
        self.SpAtk = int(SpAtk)
        self.SpDef = int(SpDef)
        self.Speed = int(Speed)
        self.Generation = int(Generation)
        self.Legendary = bool(Legendary)

    def __str__(self):
        return str(self.Number) + " | " + self.Name

    def __lt__(self, other):
        return self.Number < other.Number

    def get_types(self):
        return self.Type1, self.Type2

    def get_stats(self):
        return {"HP": self.HP,
                "Attack": self.Attack,
                "Defense": self.Defense,
                "SpAtk": self.SpAtk,
                "SpDef": self.SpDef,
                "Speed": self.Speed
                }
#
#
def get_pokemon_list(filename):
    with open(filename, encoding="utf8") as fil:
        rubrikrad = fil.readline()
        datarad = fil.readline()
        pokemon_list = []
        while datarad:
            pokemon_list.append(Pokemon(*(datarad.strip().split(","))))
            datarad = fil.readline()

    return pokemon_list
#
#
# Hash table
#class DictHash:
#
#    def __init__(self):
#        self.dictionary = {}
#
#    def store(self, key, data):
#        self.dictionary[key] = data
#
#    def search(self, key):
#        try:
#            return self.dictionary[key]
#        except KeyError:
#            return "KeyError"
#
#    def __contains__(self, item):
#        if item in self.dictionary:
#            return True
#        else:
#            return False
#
#    def __getitem__(self, key):
#        return self.dictionary[key]
#
#
#D = DictHash()

# D.store("1", "hi")
# if "1" in D:
#     print(D["1"])
# else:
#     pass

list_pokémon = get_pokemon_list("pokemon.csv")
#for pokémon in list_pokémon:
#    D.store(pokémon.Name, pokémon)

#print(D.search("Ivysaur"))
#print(D.search("Ivysau"))
#print(D["Ivysaur"])


# Hashtable with own hashing and collision resolution + nodes
#class LinkedList:
#    pass


class Node:
    def __init__(self, key="", data=None, next_node=None):
        self.key = key
        self.data = data
        self.next = next_node


class Hashtable:
    def __init__(self, size):
        self.size = size
        self.list = [None] * size

    def store(self, key, data):
        hashed_key = self.hash_function(key)
        if self.list[hashed_key] is None:
            self.list[hashed_key] = Node(key, data)
        elif self.list[hashed_key].key == key:
            self.list[hashed_key].data = data
        else:
            searching = True
            current_node = self.list[hashed_key]
            while searching:
                if current_node.next is None:
                    current_node.next = Node(key, data)
                    searching = False
                elif self.list[hashed_key].key == key:
                    self.list[hashed_key].data = data
                    searching = False
                else:
                    current_node = current_node.next

    def search(self, key):
        hashed_key = self.hash_function(key)
        if self.list[hashed_key] is None:
            raise KeyError
        else:
            current_node = self.list[hashed_key]
            if current_node.key == key:
                return current_node.data
            searching = True
            while searching:
                if current_node.next is None:
                    return None
                elif current_node.next.key == key:
                    return current_node.next.data
                else:
                    current_node = current_node.next

    def hash_function(self, key):
        hash_sum = 0
        weight = 1
        for pos in range(len(key)):
            hash_sum += ord(key[pos])*weight
            weight += 1
        return hash_sum % self.size


D = Hashtable(len(list_pokémon)*10)
for pokémon in list_pokémon:
    print(pokémon.Name)
    print(D.hash_function(pokémon.Name))
    D.store(pokémon.Name, pokémon)

print(D.search("Nidoking"))
test_poke = list_pokémon[3]
print(test_poke.Name)
print("hi")
print(D.search(test_poke.Name).Name)

T = Node("1", "2")
S = Node("3", "4", T)
Q = Node("5", "6", S)
print(Q.next.next.data)

