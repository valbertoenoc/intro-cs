x0 = int(input())
y0 = int(input())
x1 = int(input())
y1 = int(input())

dist = ((x1 - x0)**2 + (y1 - y0) ** 2) ** 0.5

if dist >= 10:
    print('longe')
else:
    print('perto')