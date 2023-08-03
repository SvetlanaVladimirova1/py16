import pytest


def test_perimeter():
     assert 23 != calc_perimeter(5, 7)


def test_area():
    assert 25 == calc_area(5, 5)


def calc_perimeter(width: float, heigth: float) -> float:
    return (width + heigth) * 2


def calc_area(width: float, heigth: float) -> float:
    b = heigth * width
    return b


if __name__ == '__main__':
    pytest.main(['-vv'])
