import  math


class Circle:
    def __init__(self, r: float):
        self.radius = r

    def calc_perimeter(self):
        return round((self.radius * math.pi * 2),2)

    def calc_area(self):
        return round((math.pi * self.radius ** 2),2)


rez = Circle(5)
print(rez.calc_perimeter())
print(rez.calc_area())
