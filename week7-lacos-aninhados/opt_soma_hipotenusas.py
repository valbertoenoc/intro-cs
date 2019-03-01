def e_hipotenusa(n):
    for c1 in range(n):
        for c2 in range(n):
            if n ** 2 == (c1 ** 2) + (c2 ** 2):
                return True
    
    return False


def soma_hipotenusas(n):
    numeros = []
    for i in range(n+1):
        if e_hipotenusa(i):
            numeros.append(i)

    print(numeros)
    return sum(numeros)


print(soma_hipotenusas(25))