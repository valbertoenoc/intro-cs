def dimensoes(matriz):
    altura = len(matriz)
    largura = len(matriz[0])

    return (altura, largura)


def soma_matrizes(A, B):
    if not dimensoes(A) == dimensoes(B):
        return False
    
    C = list(A)

    for i in range(len(C)):
        for j in range(len(C[0])):
            C[i][j] = A[i][j] + B[i][j]

    return C
