n = input('Digite um número inteiro: ')

adj_equal = False
for i, d in enumerate(n):
    if len(n) == 2:
        if n[0] == n[1]:
            adj_equal = True
            break

    if i == 0 or i == len(n) - 1:
        continue
    else:
        if d == n[i-1] or d == n[i+1]:
            adj_equal = True
            break

if adj_equal:
    print('sim')
else:
    print('não')