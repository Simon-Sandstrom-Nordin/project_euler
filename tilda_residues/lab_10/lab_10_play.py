from linkedQFile import LinkedQ
from tilda_residues.lab_10.molgrafik import Molgrafik


class Ruta:
    def __init__(self, atom="()", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


class Syntaxfel(Exception):
    pass


atomer = """H  He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr Mn  Fe  Co 
 Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd In  Sn  Sb  Te  I   Xe  Cs  Ba  
 La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf Ta  W  Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  
 Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm Bk  Cf  Es  Fm  Md  No  Lr Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv"""\
    .rstrip("\n").split()


def check_atom(q):
    if q.peek() == "(":
        return
    cap = check_capital(q)
    lower = check_case(q)
    atm = cap + lower
    if atm not in atomer:
        raise Syntaxfel("Okänd atom")


def check_capital(q):
    if q.peek() is None:
        return ""
    try:
        if q.peek() in "ABCDEFGHIJKLMNOPQRTSUVWXYZ":
            return q.dequeue()
    except AttributeError:
        pass
    raise Syntaxfel("Saknad stor bokstav")


def check_case(q):
    if q.peek() is None:
        return ""
    try:
        if q.peek() in "abcdefghijklmnopqrstuvwxyz":
            lower = q.dequeue()
            # if q.peek() in "abcdefghijklmnopqrstuvwxyz":
            #     raise Syntaxfel("Två små bokstäver")
            return lower
    except TypeError:
        pass
    return ""


def check_group(q):
    rutan = Ruta()
    check_atom(q)
    ruta.atom = readatom(q)
    check_number(q)
    ruta.num = readnum
    check_parenthesis(q)
    # grupp?
    check_molecule(q)


def check_molecule(q):
    if q.peek() is None or q.peek() == ")":
        return
    if q.peek() in "0123456789":
        return
    check_group(q)


def check_number(q, on_group=False):
    if q.peek() is None:
        if on_group:
            raise Syntaxfel("Saknad siffra")
        else:
            return

    if q.peek() not in "0123456789":
        if on_group:
            raise Syntaxfel("Saknad siffra")
        else:
            return
    try:
        char = q.dequeue()
        if char in "123456789":
            if char == "1":
                if q.peek() is None or q.peek() not in "0123456789":
                    raise Syntaxfel("För litet tal")

            while char in "0123456789":
                if q.peek() is None or q.peek() not in "0123456789":
                    return
                char = q.dequeue()

            return
    except AttributeError:
        pass
    raise Syntaxfel("För litet tal")


def check_parenthesis(q):
    if q.peek() == "(":
        q.dequeue()
        check_molecule(q)
        if q.peek() == ")":
            q.dequeue()
            check_number(q, on_group=True)
        else:
            raise Syntaxfel("Saknad högerparentes")
    else:
        return


def check_syntax(molecule):
    q = store_molecule(molecule)
    try:
        while q.peek() is not None:
            check_molecule(q)
            if q.peek() is None:
                break
            if q.peek() == ")" or q.peek() in "0123456789":
                raise Syntaxfel("Felaktig gruppstart")

        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as error:
        return str(error) + " vid radslutet " + string_queue(q)


def store_molecule(molecule):
    q = LinkedQ()
    molecule = [char for char in molecule]
    for char in molecule:
        q.enqueue(char)
    return q


def user_input():
    try:
        input_string = input().strip()
        while input_string != "#":
            molecule = input_string
            result = check_syntax(molecule)
            input_string = input().strip()
    except EOFError:
        pass


def main():
    mol = user_input()
    mg = Molgrafik()
    mg.show(mol)
    # weight(mol)


if __name__ == "__main__":
    main()
