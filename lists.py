from helper import produce_stars

agenda = [
    "Lists",
]

monday = [
    'Arroz',
    'Banana Frita',
    'Little rat'
]
tuesday = [
    'Arroz',
    'Feijão'
]
wednesday = [
    'Banana',
    'Pão',
    'Salsicha'
]
thursday = [
    'Arroz'
]
friday = [
    'Pizza'
]

menu = [monday, tuesday, wednesday, thursday, friday]

print(produce_stars(20), agenda[0], produce_stars(20), end="\n")

print("Imagine you want to store a collection of drinks", ["Beer", "Coffee", "Snake Wine"])
print("Imagine the menu of your favorite restaurant (Ratinho i.e)", menu)
print("Let's suppose you want to check the menu for monday", menu[0])
print("Important! Lists are 0 indexed and accepts all types", ["Little rat", 1, 3.4j])

