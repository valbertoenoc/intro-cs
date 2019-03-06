lista = []

while True:
    a = int(input())

    if a == 0: 
        break
    
    lista.append(a)


def inverte(lista):
    return lista[::-1]


for i in inverte(lista):
    print(i)