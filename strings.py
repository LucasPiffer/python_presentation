from helper import produce_stars

agenda = [
    "Assigning to a variable",
    "Operations on strings"
]

print(produce_stars(20), agenda[0], produce_stars(20), end="\n")

my_name_is = "Sheldon Cooper"
print(my_name_is)

print(produce_stars(20), agenda[1], produce_stars(20), end="\n")

print("Only name:", my_name_is[0:7])
print("Replacing:", my_name_is.lower())
print("Uppercase:", my_name_is.upper())
print("Title:", my_name_is.title())
print("Join:", "^^^^".join(my_name_is))
print("Split:", "piffer.lucas@gmail.com".split('@') )
print("Replacing piffer.lucas@gmail.com to:", "piffer.lucas@gmail.com".replace("piffer.lucas", "sheldon.cooper"))
print("Concatenation", "Lucas" + " Piffer")