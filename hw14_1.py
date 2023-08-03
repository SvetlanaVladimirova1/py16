import unittest


class TestValue(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(24, calc_perimeter(5, 7))

    def test_perimeter_not_eq(self):
        self.assertNotEqual(25, calc_perimeter(5, 7))

    def test_area(self):
        self.assertEqual(25, calc_area(5, 5))

    def test_area_not_eq(self):
        self.assertNotEqual(23, calc_area(5, 5))


def calc_perimeter(width: float, heigth: float) -> float:
    return (width + heigth) * 2


def calc_area(width: float, heigth: float) -> float:
    b = heigth * width
    return b


if __name__ == '__main__':
    unittest.main(verbosity=2)
