from linkedQFile import LinkedQ


class Syntaxfel(Exception):
    pass


def check_molecule(q):
    check_atom(q)
    check_number(q)


def check_atom(q):
    check_capital(q)
    check_case(q)


def check_capital(q):
    try:
        if q.peek() in "ABCDEFGHIJKLMNOPQRTSUVWXYZ":
            q.dequeue()
            return
    except AttributeError:
        pass
    raise Syntaxfel("Saknad stor bokstav")


def check_case(q):
    case_alphabet = "abcdefghijklmnopqrstuvwxyz"
    try:
        if q.peek() in case_alphabet:
            q.dequeue()
        if q.peek() in case_alphabet:
            raise Syntaxfel("Två små bokstäver")
    except TypeError:
        pass
    return


def check_number(q):
    if q.peek() is None:
        return

    try:
        char = q.dequeue()
        if char in "123456789":
            if char == "1":
                q.dequeue()
            return
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
        check_molecule(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as error:
        return str(error) + " vid radslutet " + string_queue(q)


def main():
    input_string = input().strip()
    while input_string != "#":
        molecule = input_string
        result = check_syntax(molecule)
        print(result)
        input_string = input().strip()


if __name__ == "__main__":
    main()
