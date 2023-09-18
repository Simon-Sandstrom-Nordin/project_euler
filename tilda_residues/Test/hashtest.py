from tilda_residues.Test.my_hash_table import Hashtable
import unittest


class TestHashtable(unittest.TestCase):

    def test_store(self):
        print("\nTries to store an atom with its name as its key")
        name = "He"
        weight = 4.002602
        atom = Atom(name, weight)
        hash_table = Hashtable(3)
        hash_table.store(name, atom)

    def test_search(self):
        print("\nTries to store an atom and then remove it")
        name = "He"
        weight = 4.002602
        atom = Atom(name, weight)
        hash_table = Hashtable(3)
        hash_table.store(name, atom)
        x = hash_table.search(name)
        self.assertIsInstance(x, Atom)
        self.assertEqual(x.get_name(), name)
        self.assertEqual(x.get_weight(), weight)

    def test_find_all(self):
        print("\nTries to store all atoms then search for each one")
        atom_list = create_atom_list()
        hash_table = store_hash_table(atom_list)
        self.assertTrue(all_atoms_exist(hash_table, atom_list))

    def test_fail(self):
        print("\nTries to search for an atom not stored")
        atom_list = create_atom_list()
        hash_table = store_hash_table(atom_list)
        self.assertFalse(crazy_atom_exists(hash_table))


class Atom:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "{" + self.name + " " + str(self.weight) + "}"

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight


def create_atom_list():
    """Skapar och returnerar en lista med Atom-objekt"""
    atom_data = "H  1.00794;\
    He 4.002602;\
    Li 6.941;\
    Be 9.012182;\
    B  10.811;\
    C  12.0107;\
    N  14.0067;\
    O  15.9994;\
    F  18.9984032;\
    Ne 20.1797;\
    Na 22.98976928;\
    Mg 24.3050;\
    Al 26.9815386;\
    Si 28.0855;\
    P  30.973762;\
    S  32.065;\
    Cl 35.453;\
    K  39.0983;\
    Ar 39.948;\
    Ca 40.078;\
    Sc 44.955912;\
    Ti 47.867;\
    V  50.9415;\
    Cr 51.9961;\
    Mn 54.938045;\
    Fe 55.845;\
    Ni 58.6934;\
    Co 58.933195;\
    Cu 63.546;\
    Zn 65.38;\
    Ga 69.723;\
    Ge 72.64;\
    As 74.92160;\
    Se 78.96;\
    Br 79.904;\
    Kr 83.798;\
    Rb 85.4678;\
    Sr 87.62;\
    Y  88.90585;\
    Zr 91.224;\
    Nb 92.90638;\
    Mo 95.96;\
    Tc 98;\
    Ru 101.07;\
    Rh 102.90550;\
    Pd 106.42;\
    Ag 107.8682;\
    Cd 112.411;\
    In 114.818;\
    Sn 118.710;\
    Sb 121.760;\
    I  126.90447;\
    Te 127.60;\
    Xe 131.293;\
    Cs 132.9054519;\
    Ba 137.327;\
    La 138.90547;\
    Ce 140.116;\
    Pr 140.90765;\
    Nd 144.242;\
    Pm 145;\
    Sm 150.36;\
    Eu 151.964;\
    Gd 157.25;\
    Tb 158.92535;\
    Dy 162.500;\
    Ho 164.93032;\
    Er 167.259;\
    Tm 168.93421;\
    Yb 173.054;\
    Lu 174.9668;\
    Hf 178.49;\
    Ta 180.94788;\
    W  183.84;\
    Re 186.207;\
    Os 190.23;\
    Ir 192.217;\
    Pt 195.084;\
    Au 196.966569;\
    Hg 200.59;\
    Tl 204.3833;\
    Pb 207.2;\
    Bi 208.98040;\
    Po 209;\
    At 210;\
    Rn 222;\
    Fr 223;\
    Ra 226;\
    Ac 227;\
    Pa 231.03588;\
    Th 232.03806;\
    Np 237;\
    U  238.02891;\
    Am 243;\
    Pu 244;\
    Cm 247;\
    Bk 247;\
    Cf 251;\
    Es 252;\
    Fm 257;\
    Md 258;\
    No 259;\
    Lr 262;\
    Rf 265;\
    Db 268;\
    Hs 270;\
    Sg 271;\
    Bh 272;\
    Mt 276;\
    Rg 280;\
    Ds 281;\
    Cn 285"

    atom_list = []
    lista = atom_data.split(";")
    for name_weight in lista:
        name, weight = name_weight.split()
        atom = Atom(name, float(weight))
        atom_list.append(atom)
    return atom_list


def store_hash_table(atom_list):
    """Lagrar atomlistans element i en hashtabell"""
    number_of_elements = len(atom_list)
    hash_table = Hashtable(number_of_elements)
    for atom in atom_list:
        hash_table.store(atom.name, atom)
    return hash_table


def all_atoms_exist(hash_table, atom_list):
    """Kan man hitta alla atomer i hashtabellen?"""
    number = 0
    ok = True
    for control_atom in atom_list:
        name, weight = control_atom.get_name(), control_atom.get_weight()
        weight = float(weight)
        try:
            hashed_atom = hash_table.search(name)
            if hashed_atom.weight != weight:
                print(name, "has incorrect weight.")
            else:
                number += 1
        except KeyError:
            print(name, "did not exist in the hash table.")
            ok = False
    return ok


def crazy_atom_exists(hash_tabel):
    """Does the hash table return KeyError because the atom doesn't exist?"""
    crazy_atom = "Zz"
    try:
        x = hash_tabel.search(crazy_atom)
        # crazy atom was stored in the hash table
        return True
    except KeyError:
        # crazy atom wasn't stored in the hash table
        return False


if __name__ == "__main__":
    unittest.main()
