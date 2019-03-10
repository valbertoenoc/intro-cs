class Triangulo():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.lados = sorted([self.a,self.b,self.c])

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isósceles'
        else:
            return 'escaleno'

    def retangulo(self):
        return (self.a ** 2 + self.b ** 2) == self.c ** 2 or \
               (self.a ** 2 + self.c ** 2) == self.b ** 2 or \
               (self.c ** 2 + self.b ** 2) == self.a ** 2

    def semelhantes(self, triangulo):
        r = sum(self.lados) / sum(triangulo.lados)
        return all(k / z == r for k, z in zip(self.lados, triangulo.lados))
