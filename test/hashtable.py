# The shit where we made our own hash tables.

class DictHash:

    def __init__(self):
        self.dict = {}

    def store(self, key, data):
        self.dict[key] = data

    def search(self, key):
        try:
            return self.dict[key]
        except KeyError:
            return "Key does not correspond to any data"

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        try:
            return self.dict[key] is not None
        except KeyError:
            return False


d = DictHash()
d.store("1", "one")
print(d.search("1"))
print(d["1"])
print("2" in d)


# Next will be to test this with the Pokédex cvs file... again.

# Stolen from pokemon.py
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


def get_pokemon_dict(filename):
    with open(filename, encoding="utf8") as fil:
        rubrikrad = fil.readline()  # unwanted row, redundant
        datarad = fil.readline()
        pokemon_dict = DictHash()
        while datarad:  # when datarad becomes \n?
            pokemon_dict.store(datarad.strip().split(",")[1], Pokemon(*(datarad.strip().split(","))))
            datarad = fil.readline()    # read new row
    return pokemon_dict


class HashNode:

    def __init__(self, key="", data=None):
        self.key = key
        self.data = data


class HashTable:

    def __init__(self, size):
        self.list = [None] * size   # I got a list

    def store(self, key, data):
        # först utan krockhantering
        self.list[key] = HashNode(key, data)

    def search(self, key):
        return self.list[key]

    @staticmethod
    def hash_function(self, object):
        return object


def main():
    poke_dict = get_pokemon_dict("pokemon.csv")
    print(poke_dict.search("Xerneass"))
    tab = HashTable(10)
    print(tab)
    tab.store(2, "b")
    #print(tab.search(1).data)
    print(tab.search(2).data)


main()

# Hashtabell, samma som DictHash. HashNode klass för tabellens noder.
# Noder har både nyckel och värde. Lagom stor tabell.
# Egen hashfunktion, med bra fördelning (redovisning av denna:
# teoretisk analys eller genm mätning av max antal krockar).
# Krockhantering: probing eller listor
# KeyError används för att indikera att nyckel ej finns.
