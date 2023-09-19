import unittest
from calculator import Calculator

calculadora = Calculator()

class TestSoma(unittest.TestCase):

    def test_soma_positivos(self):
        self.assertEqual(calculadora.somar(2,3), 5)

    def test_soma_negativos(self):
        self.assertEqual(calculadora.somar(-1,-1), -2)


unittest.main()