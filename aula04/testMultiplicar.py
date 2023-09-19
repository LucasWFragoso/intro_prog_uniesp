import unittest
from calculator import Calculator

calculadora = Calculator()

class TestMultiplicar(unittest.TestCase):

    def test_multiplicar_dois_por_tres(self):
        self.assertEqual(calculadora.multiplicar(2,3), 6)


unittest.main()