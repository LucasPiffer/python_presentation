import math
from helper import produce_stars

agenda = [
    'Basic operations on different number types',
    'Number type conversion',
    'Math functions'
]

age = 28
my_float_number = 0.4 + .34
negative_float_number = -23.4

print(produce_stars(20), agenda[0], produce_stars(20), end="\n")

print("Division", age / my_float_number)
print("Sum", age + my_float_number)
print("Multiplication", age * 2)
print("Exponent", 2 ** 2)
print("Modulus operator", 20 % 2, "When remainder is not 0", 10 % 3)
print("Floor division", age // 3)

print(produce_stars(20), agenda[1], produce_stars(20), end="\n")

print("To integer, from 30.4 to", int(30.4))
print("To float, from 30 to", float(30))

print(produce_stars(20), agenda[2], produce_stars(20), end="\n")

print('Absolute value of x', abs(-30))
print('Ceil', math.ceil(30.5))
print('Floor', math.floor(22.34))