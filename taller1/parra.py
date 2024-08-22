# Interseccion
if __name__ == '__main__':
    print("hi")

def intersec(a: list, b: list) -> list:
    return list(filter(lambda x: x in b, a))


def interseccion(*args: list) -> list:
    if (len(args) < 1): return []
    res: list = args[0]

    for i in range(1, len(args)):
        res = intersec(res, args[i])
    return res

def diferencia_simetrica(a: list, b: list) -> list:
    return
