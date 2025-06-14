import unittest
from conversor import converter

class TestConversor(unittest.TestCase):
    def test_dolar_para_real(self):
        self.assertEqual(converter(1, 'USD', 'BRL'), 5.25)

    def test_real_para_dolar(self):
        self.assertEqual(converter(5.25, 'BRL', 'USD'), 1.0)

    def test_euro_para_real(self):
        self.assertEqual(converter(1, 'EUR', 'BRL'), 5.9)

    def test_real_para_euro(self):
        self.assertEqual(converter(5.9, 'BRL', 'EUR'), 1.0)

    def test_dolar_para_euro(self):
        self.assertAlmostEqual(converter(1, 'USD', 'EUR'), 1.12, places=2)

    def test_moeda_invalida(self):
        with self.assertRaises(ValueError):
            converter(10, 'BTC', 'USD')

if __name__ == '__main__':
    unittest.main()
