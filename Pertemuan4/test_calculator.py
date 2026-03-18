import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_tambah(self):
        self.assertEqual(self.calc.tambah(5, 3), 8)

    def test_kurang(self):
        self.assertEqual(self.calc.kurang(10, 4), 6)

    def test_kali(self):
        self.assertEqual(self.calc.kali(6, 2), 12)

    def test_bagi(self):
        self.assertEqual(self.calc.bagi(8, 2), 4)

    def test_bagi_nol(self):
        with self.assertRaises(ValueError):
            self.calc.bagi(5, 0)

    def test_modulus(self):
        self.assertEqual(self.calc.modulus(10, 3), 1)

    def test_pangkat(self):
        self.assertEqual(self.calc.pangkat(2, 3), 8)

    def test_pembagian_bulat(self):
        self.assertEqual(self.calc.pembagian_bulat(10, 3), 3)

    def test_modulus_nol(self):
        with self.assertRaises(ValueError):
            self.calc.modulus(5, 0)

    def test_pembagian_bulat_nol(self):
        with self.assertRaises(ValueError):
            self.calc.pembagian_bulat(5, 0)


if __name__ == "__main__":
    unittest.main()