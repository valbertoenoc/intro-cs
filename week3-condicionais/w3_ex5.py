numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

numeros = [numero1, numero2, numero3]

if numero1 > numero2 or numero1 > numero3 or numero2 > numero3:
    print('não está em ordem crescente')
else:
    print('crescente')
