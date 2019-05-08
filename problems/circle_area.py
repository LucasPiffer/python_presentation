import math


def formula_circle_area():
    def area(r):
        return math.pi * r ** 2

    return area


formula = formula_circle_area()
print(formula(1))
