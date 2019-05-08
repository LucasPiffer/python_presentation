'''
self.name => public
self._name => proteced
self.__name => private
'''


class LivingBeing:
    _name = ''
    _specie = 'Living Being'

    def __init__(self, name):
        self._name = name

    def get_specie(self):
        return self._specie

    def get_name(self):
        return self._name


class Cat(LivingBeing):
    def __init__(self, name):
        super().__init__(name)
        self._specie = 'cat'


class Human(LivingBeing):
    def __init__(self, name):
        super().__init__(name)
        self._specie = 'human'


class RoberFredo(Cat, Human):
    def get_sound(self):
        return "Pluplu"


alfredo = Human('Alfredo')
roberto = Cat('Roberto')
roberFredo = RoberFredo('Roberto Alfredo')


print(alfredo.get_name() + " is a " + alfredo.get_specie())
print(roberto.get_name() + " is a " + roberto.get_specie())
print(roberFredo.get_name() + " is a cat? ", isinstance(roberFredo, Cat), 'is a human?', isinstance(roberFredo, Human))
