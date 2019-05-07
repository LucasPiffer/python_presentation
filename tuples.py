from helper import produce_stars

agenda = [
    "Tuples",
    "Accessing values",
    "Updating values",
    "Operations"
]

definition = "A sequence of immutable Python objects"

print(produce_stars(20), agenda[0], produce_stars(20), end="\n")

my_first_tuple = ("My", "My" "first", "tuple")

print("printing a tuple", my_first_tuple)
print("tuple constructor", tuple(('Lucas', 'Piffero')))
print("Checking the type:", type(my_first_tuple).__name__)

print(produce_stars(20), agenda[1], produce_stars(20), end="\n")
print("use square brackets like that my_first_tuple[0]", my_first_tuple[0])

#print(produce_stars(20), agenda[2], produce_stars(20), end="\n")
#my_first_tuple[0] = "An exception is expected since tuples are unchangeable"

print(produce_stars(20), agenda[3], produce_stars(20), end="\n")
print('Obtaining the size of a tuple', len(my_first_tuple))
print('concatenation', (1, 2, 3, 4) + (4, 5, 6, 7, 8))
print('Repetition', (1, ) * 4 )
print('Membership', 3 in (1, 2, 3))




