def union_conjuntos_recursiva(*conjuntos: list, pos: int, conjunto_aux: list) -> None:

    if pos > conjuntos.count:
        return conjunto_aux

    return union_conjuntos_recursiva(conjuntos, pos+1, union_conjuntos(conjunto_aux, conjuntos[pos]))

def union_conjuntos(conjunto1: list, conjunto2: list) -> list:
    for elemento1 in conjunto1:
        if elemento1 not in conjunto2:
            conjunto2.append(elemento1)
    return conjunto2
