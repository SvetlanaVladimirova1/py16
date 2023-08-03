import unittest
from hw14_4 import Circle


class TestCaseName(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Circle(5)

    def test_perimeter(self):
        self.assertEqual(self.r1.calc_perimeter(), 31.42)

    def test_area(self):
        self.assertEqual(self.r1.calc_area(), 78.54)


if __name__ == '__main__':
    unittest.main(verbosity=2)
