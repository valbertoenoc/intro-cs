def imprime_matriz(matriz):
    a = len(matriz)
    l = len(matriz[0])
    for i in range(a):
        for j in range(l):
            if not j == l - 1:
                print(matriz[i][j], end=' ')
            else:
                print(matriz[i][j])

