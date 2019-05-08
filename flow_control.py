class Person:
    def __init__(self, name, age):
        self.__name__ = name
        self.__age__ = age

    def get_name(self):
        return self.__name__

    def get_age(self):
        return self.__age__


def factory(name, age):
    return Person(name, age)


def can_drink(person):
    if person.get_age() < 18:
        return 'can NOT drink'
    elif person.get_age() >= 18 and person.get_age() < 65:
        return 'can drink'
    else:
        return 'Must drink'


people = [
    factory('Alfredo', 34),
    factory('Mariazinha', 14),
    factory('Roberto', 68)
]

for person in people:
    print(person.get_name() + " ", person.get_age(), "Can drink?", can_drink(person))

