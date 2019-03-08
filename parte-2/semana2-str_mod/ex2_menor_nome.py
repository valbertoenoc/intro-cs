def menor_nome(nomes):
    nomes_ordenados = sorted(nomes, key=lambda x: len(x.strip()))

    return nomes_ordenados[0].strip().capitalize()