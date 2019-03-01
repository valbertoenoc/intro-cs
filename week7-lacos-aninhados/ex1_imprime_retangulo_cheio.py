largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))

for _ in range(altura):
    for _ in range(largura):
        print('#', end='')
    print()