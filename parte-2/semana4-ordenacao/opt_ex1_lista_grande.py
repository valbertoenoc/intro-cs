import random

def lista_grande(n):
    lst = []
    for _ in range(n):
        lst.append(random.randint(0, n))
    
    return lst
