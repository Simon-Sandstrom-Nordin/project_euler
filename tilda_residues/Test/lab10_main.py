from linkedQFile import LinkedQ
from tilda_residues.Test.molgrafik import Molgrafik
from tilda_residues.Test.mol_weight import molar_weight
atoms = """H  He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr Mn  Fe  Co 
 Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd In  Sn  Sb  Te  I   Xe  Cs  Ba  
 La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf Ta  W  Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  
 Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm Bk  Cf  Es  Fm  Md  No  Lr Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv""".rstrip(
    "\n").split()


class Syntaxfel(Exception):
    pass


class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


def check_molecule(q):
    if q.peek() is None or q.peek() == ")":
        return
    if q.peek() in "0123456789":
        return
    mol = check_group(q)
    return mol


def check_group(q):
    rutan = Ruta()  # Rotnod
    rutan.atom = check_atom(q)
    rutan.num = check_number(q)
    if q.peek() == "(":
        if rutan.atom is None:
            rutan.next = rutan
            rutan.atom = "( )"
        else:
            rutan.next = Ruta() # tom nod
        q.dequeue()
        rutan.next.down = check_molecule(q) # inre molekyl/ undergrupp
        if q.peek() == ")":
            q.dequeue()
            rutan.next.num = check_number(q, on_group=True)
        else:
            raise Syntaxfel("Saknad högerparentes")
        rutan.next.next = check_molecule(q)
    else:
        rutan.next = check_molecule(q)
    return rutan


def check_atom(q):
    if q.peek() == "(":
        return None
    cap = check_capital(q)
    lower = check_case(q)
    atom = cap + lower
    if atom not in atoms:
        raise Syntaxfel("Okänd atom")
    return atom


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
            return lower
    except TypeError:
        pass
    return ""


def check_number(q, on_group=False):
    if q.peek() is None:
        if on_group:
            raise Syntaxfel("Saknad siffra")
        else:
            return 1

    if q.peek() not in "0123456789":
        if on_group:
            raise Syntaxfel("Saknad siffra")
        else:
            return 1
    try:
        char = q.dequeue()
        num = []
        num.append(char)
        if char in "123456789":
            if char == "1":
                if q.peek() is None or q.peek() not in "0123456789":
                    raise Syntaxfel("För litet tal")

            while char in "0123456789":
                if q.peek() is None or q.peek() not in "0123456789":
                    return int(''.join([str(n) for n in num]))
                char = q.dequeue()
                num.append(char)

            return int(''.join([str(n) for n in num]))
    except AttributeError:
        pass
    raise Syntaxfel("För litet tal")


def store_molecule(molecule):
    q = LinkedQ()
    molecule = [char for char in molecule]
    for char in molecule:
        q.enqueue(char)
    return q


def string_queue(q):
    string = ""
    while not q.is_empty():
        char = q.dequeue()
        string += char
    return string


def check_syntax(molecule):
    q = store_molecule(molecule)
    try:
        while q.peek() is not None:
            ruta = check_molecule(q)
            if q.peek() is None:
                mg = Molgrafik()
                mg.show(ruta)
                print(molar_weight(ruta))
                break
            if q.peek() == ")" or q.peek() in "0123456789":
                raise Syntaxfel("Felaktig gruppstart")

        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as error:
        return str(error) + " vid radslutet " + string_queue(q)


def user_input():
    try:
        input_string = input().strip()
        while input_string != "#":
            molecule = input_string
            result = check_syntax(molecule)
            print(result)
            input_string = input().strip()
    except EOFError as e:
        pass


def string_in(input_str):
    all_result = []
    input_string = input_str.rstrip("\n").split()
    for molecule in input_string:
        if molecule == "#":
            break
        result = check_syntax(molecule)
        # print(result)
        all_result.append(result)

    return "\n".join(all_result) + "\n"


if __name__ == "__main__":
    user_input()
