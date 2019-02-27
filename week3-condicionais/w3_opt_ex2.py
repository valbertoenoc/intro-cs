a = int(input())
b = int(input())
c = int(input())

delta = b**2 - 4*a*c

if delta < 0:
    print('esta equação não possui raízes reais')
elif delta == 0:
    x = (-b + delta ** 0.5) / (2*a)
    print('a raiz desta equação é {}'.format(x))
elif delta > 0:
    x1 = (b*-1 + delta ** 0.5) / (2*a)
    x2 = (b*-1 - delta ** 0.5) / (2*a)

    if x1 > x2:
        x1, x2 = x2, x1 

    print('as raízes da equação são {} e {}'.format(x1, x2))
        