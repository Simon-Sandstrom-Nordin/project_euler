from tilda_residues.Test.molgrafik import *


class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


mol = Ruta(atom="Xe", num=3)
mg = Molgrafik()
mg.show(mol)
