import os
from tilda_residues.Test.lab1 import Pokemon
from tilda_residues.Test.DictHash import DictHash
from tilda_residues.Test.my_hash_table import Hashtable
from tilda_residues.Test.song import Song


def get_dicthash():
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(ROOT_DIR, 'Test/pokemon.csv')
    with open(filename, encoding="utf8") as fil:
        rubrikrad = fil.readline()
        datarad = fil.readline()
        poke_hashtable = DictHash()
        while datarad:
            pokemon_obj = (Pokemon(*(datarad.strip().split(","))))
            poke_hashtable.store(pokemon_obj.Name, pokemon_obj)
            datarad = fil.readline()

    return poke_hashtable


def get_my_hash(size):
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(ROOT_DIR, 'Test/pokemon.csv')
    with open(filename, encoding="utf8") as fil:
        rubrikrad = fil.readline()
        datarad = fil.readline()
        poke_hashtable = Hashtable(size=size)
        while datarad:
            pokemon_obj = (Pokemon(*(datarad.strip().split(","))))
            poke_hashtable.store(pokemon_obj.Name, pokemon_obj)
            datarad = fil.readline()

    return poke_hashtable


def get_song_list_hashtable():
    song_list = read_song_list('C:/Users/manip/OneDrive/Desktop/Programming/Github/project_euler/tilda_residues/Test/unique_tracks.txt')
    print("Length of song list")
    print(len(song_list))
    hash_table = Hashtable(size=len(song_list) * 2)
    #hash_table = Hashtable(size=len(song_list) // 10)
    for song in song_list:
        hash_table.store(song.trackid, song)
    print("Load factor of table:")
    print(hash_table.get_load_factor())
    print("Max collisions in table:")
    print(hash_table.get_max_collisions())
    return hash_table


def read_song_list(file_name):
    with open(file_name, encoding="utf8") as file:
        line = file.readline()
        song_list = []
        while line:
            song_list.append(Song(*(line.strip().split("<SEP>"))))
            line = file.readline()
    return song_list


def test(hash_table):
    temp_poke = hash_table['Weedle']
    print(temp_poke)
    print(temp_poke.get_types())

    temp_poke = hash_table.search('Yveltal')
    print(temp_poke)
    print(temp_poke.get_types())

    try:
        temp_poke = hash_table['asuidabuid']
        print(temp_poke)
    except KeyError:
        print("Not Found")

    print(hash_table.get_load_factor())


if __name__ == "__main__":
    test(get_my_hash(size=1500))
    song_hash_table = get_song_list_hashtable()
    temp_song = song_hash_table['TRJAGVH128F933A57A']
    print(temp_song)
    print()
