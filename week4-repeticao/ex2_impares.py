n = int(input('Digite o valor de n: '))

i = 0
n_i = 1
while i < n:
    if n_i % 2 != 0:
        print(n_i)
        n_i += 2
    i += 1
    