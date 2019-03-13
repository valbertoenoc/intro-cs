def ordenada(lista):
    for i, n in enumerate(lista):
        if i == 0: continue

        if n < lista[i-1]:
            return False
    
    return True