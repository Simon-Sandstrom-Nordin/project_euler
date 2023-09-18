from random import shuffle


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


def get_pokemon_list(filename):
    with open(filename, encoding="utf8") as fil:
        title_row = fil.readline()
        data_row = fil.readline()
        pokemon_list = []
        while data_row:
            pokemon_list.append(Pokemon(*(data_row.strip().split(","))))

            data_row = fil.readline()

    return pokemon_list


# Search by # or name
def search_pokemon(poke_list, search_term):
    for pokemon in poke_list:

        if isinstance(search_term, str):
            if search_term.lower() == pokemon.Name.lower():
                return pokemon
        elif isinstance(search_term, int):
            if search_term == pokemon.Number:
                return pokemon

        else:
            raise TypeError("Use int for ID search or string for name search")

    return False


def main():
    poke_list = get_pokemon_list("C:/Users/manip/OneDrive/Desktop/Programming/Github/project_euler/tilda_residues/Test/pokemon.csv")

    shuffled_pokemon = poke_list
    shuffle(shuffled_pokemon)

    print("Shuffled")
    for pokemon in shuffled_pokemon[1:10]:
        print(pokemon)

    print("\n\nSorted")
    for pokemon in sorted(shuffled_pokemon[1:10]):
        print(pokemon)

    print("\n\nIs   (" + str(shuffled_pokemon[1]) + ")   >   (" + str(shuffled_pokemon[2]) + ")   ?")
    print(shuffled_pokemon[1] > shuffled_pokemon[2])

    print()

    print(shuffled_pokemon[5])
    print(shuffled_pokemon[5].get_types())
    print(shuffled_pokemon[5].get_stats())

    print()
    print()

    search_result = search_pokemon(poke_list, "charmander")
    print(search_result)
    print(search_result.get_stats())

    print()

    search_result = search_pokemon(poke_list, 351)
    print(search_result)
    print(search_result.get_stats())


if __name__ == "__main__":
    main()
