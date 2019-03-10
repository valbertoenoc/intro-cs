import unittest
from ex_class_triangulo import Triangulo

class TestTriangulo(unittest.TestCase):
    def test_perimetro(self):
        t = Triangulo(1, 2, 3)
        self.assertEqual(t.perimetro(), 6)

    def test_tipo_equilatero(self):
        t = Triangulo(2,2,2)
        self.assertEqual(t.tipo_lado(), 'equilátero')

    def test_tipo_escaleno(self):
        t = Triangulo(1,2,3)
        self.assertEqual(t.tipo_lado(), 'escaleno')

    def test_tipo_isosceles(self):
        t = Triangulo(2,2,5)
        self.assertEqual(t.tipo_lado(), 'isósceles')

    def test_retangulo(self):
        t = Triangulo(3,4,5)
        self.assertTrue(t.retangulo())

    def test_semelhantes(self):
        t1 = Triangulo(3,4,5)
        t2 = Triangulo(3,4,5)
        t3 = Triangulo(6,8,10)
        t4 = Triangulo(4,5,6)
        t5 = Triangulo(3,3,3)
        self.assertTrue(t1.semelhantes(t2))
        self.assertTrue(t1.semelhantes(t3))
        self.assertFalse(t5.semelhantes(t1))
        self.assertFalse(t1.semelhantes(t4))


if __name__ == "__main__":
    unittest.main()