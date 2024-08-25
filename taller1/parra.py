## INTERSECCIÓN
##Función solución


def clean(e : list) -> list:
    return (list)(set(e))

def interseccion(*args: list) -> list:
    for e in args: clean(e)
    if (len(args) == 0): return []
    res: list = args[0]

    for i in range(1, len(args)):
        res = intersec(res, args[i]) ##Utilizamos la función auxiliar para nuestro metodo maestro.
    return res


##Función auxiliar
def intersec(a: list, b: list) -> list:
    return list(filter(lambda x: x in b, a))

    ##DIFERENCIA SIMETRICA
    ##Función solución


def diferencia_simetrica(*args: list) -> list:
    for e in args: clean(e)
    if (len(args) == 0): return []
    res: list = args[0]

    for i in range(1, len(args)):
        res = dif_sec(res, args[i])
    return res


##Función auxiliar
def dif_sec(a: list, b: list) -> list:
    inter: list = intersec(a, b)
    union: list = union_conjuntos(a, b)
    return list(filter(lambda x: x not in inter, union))


##Metodos de Osma

def union_conjuntos(conjunto1: list, conjunto2: list) -> list:
    for elemento1 in conjunto1:
        if elemento1 not in conjunto2:
            conjunto2.append(elemento1)
    return conjunto2


##UNION
## Función solución
def union_conjuntos_recursiva(*conjuntos: list, pos: int, conjunto_aux: list) -> None:
    if pos > conjuntos.count:
        return conjunto_aux

    return union_conjuntos_recursiva(conjuntos, pos + 1, union_conjuntos(conjunto_aux, conjuntos[pos]))


## DIFERENCIA DE CONJUNTOS
## Debe tenerse en consideración que esta funcióin
# realiza la diferencia en el orden en que van indicados los parametros.


# Donde al primer conjunto se le sustraen los elementos de los demás conjuntos.
def diferencia(*args: list) -> list:
    for e in args: clean(e)
    if (len(args) == 0): return []
    res = args[0]
    for i in range(1, len(args)):
        res = dif(res, args[i])
    return res


# retoerna a menos b y no al revez.
def dif(a: list, b: list) -> list:
    return list(filter(lambda x: x not in b, a))  ##Esto quiere decir, "todos los elementos de a que no estén en b).


def main():
    lists = [
        [1, 3, 4, 7, 7, 8, 10],
        [2, 4, 5, 6, 8],
        [1, 3, 5, 8, 9]
    ]
    #print(diferencia_simetrica(lists[0], lists[1], lists[2]))
    print(clean([1,1,2,2,3,4,5,5,5,5,6,7,7]))



main()
