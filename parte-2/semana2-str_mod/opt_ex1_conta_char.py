def conta_letras(frase, contar='vogais'):
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vogais = 'aeiouAEIOU'

    cont = 0
    for c in frase:
        if contar == 'vogais':
            if c in vogais:
                cont += 1
        else:
            if c in consoantes:
                cont += 1

    return cont


print(conta_letras('programamos em python'))
print(conta_letras('programamos em python', 'vogais'))
print(conta_letras('programamos em python', 'consoantes'))