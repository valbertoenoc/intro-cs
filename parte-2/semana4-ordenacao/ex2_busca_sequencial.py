def busca(lista, elemento):
    for i, e in enumerate(lista):
        if e == elemento:
            return i
    return False