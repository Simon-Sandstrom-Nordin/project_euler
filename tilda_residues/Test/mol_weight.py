from tilda_residues.Test.hashtest import create_atom_list, store_hash_table


def molar_weight(ruta, weight=0):
    atom_hash = store_hash_table(create_atom_list())
    try:
        atom_weight = atom_hash[ruta.atom].weight
        weight += atom_weight * ruta.num
    except KeyError:
        if ruta.down is not None:
            group_weight = molar_weight(ruta.down)
            weight += group_weight * ruta.num

    if ruta.next is not None:
        weight += molar_weight(ruta.next)

    return weight
