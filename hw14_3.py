import doctest


def calc_perimeter(width: int, heigth: int) -> int:

    """
    >>> calc_perimeter(5, 7)
    24
    >>> calc_perimeter(6, 4)
    20
    """
    a = (width + heigth) * 2
    return a

def calc_area(width: int, heigth: int) -> int:
    """
    >>> calc_area(5, 5)
    25
    >>> calc_area(4, 4)
    16
    """
    b = heigth * width
    return b


if __name__ == '__main__':
    doctest.testmod(verbose=True)
