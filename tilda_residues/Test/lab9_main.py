from tilda_residues.Test.linkedQFile import LinkedQ

atoms = """
H  He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr Mn  Fe  Co 
 Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd In  Sn  Sb  Te  I   Xe  Cs  Ba  
 La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf Ta  W  Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  
 Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm Bk  Cf  Es  Fm  Md  No  Lr Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv
 """.rstrip("\n").split()


class SyntaxError(Exception):
    pass


def check_molecule(q):
    if q.peek() is None or q.peek() == ")":
        return
    if q.peek() in "0123456789":
        return
    check_group(q)


def check_group(q):
    check_atom(q)
    check_number(q)
    check_parenthesis(q)
    check_molecule(q)


def check_atom(q):
    if q.peek() == "(":
        return
    cap = check_capital(q)
    lower = check_case(q)
    atom = cap + lower
    if atom not in atoms:
        raise SyntaxError("Okänd atom")


def check_capital(q):
    if q.peek() is None:
        return ""
    try:
        if q.peek() in "ABCDEFGHIJKLMNOPQRTSUVWXYZ":
            return q.dequeue()

    except AttributeError:
        pass
    raise SyntaxError("Saknad stor bokstav")


def check_case(q):
    if q.peek() is None:
        return ""
    try:
        if q.peek() in "abcdefghijklmnopqrstuvwxyz":
            lower = q.dequeue()
            # if q.peek() in "abcdefghijklmnopqrstuvwxyz":
            #     raise SyntaxError("Två små bokstäver")
            return lower
    except TypeError:
        pass
    return ""


def check_number(q, on_group=False):
    if q.peek() is None:
        if on_group:
            raise SyntaxError("Saknad siffra")
        else:
            return

    if q.peek() not in "0123456789":
        if on_group:
            raise SyntaxError("Saknad siffra")
        else:
            return
    try:
        char = q.dequeue()
        if char in "123456789":
            if char == "1":
                if q.peek() is None or q.peek() not in "0123456789":
                    raise SyntaxError("För litet tal")

            while char in "0123456789":
                if q.peek() is None or q.peek() not in "0123456789":
                    return
                char = q.dequeue()

            return
    except AttributeError:
        pass
    raise SyntaxError("För litet tal")


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
            check_molecule(q)
            if q.peek() is None:
                break
            if q.peek() == ")" or q.peek() in "0123456789":
                raise SyntaxError("Felaktig gruppstart")

        return "Formeln är syntaktiskt korrekt"
    except SyntaxError as error:
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
    # print(atoms)
    user_input()
