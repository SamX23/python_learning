class AnimalKingdom(object):
    def __init__(self, name):
        self.lives = 1
        self.brains = True
        self.primitive = True
        self.hunger = 100
        self.tired = 100
        self.name = name

    def print_all(self):
        pass


class Mammals(AnimalKingdom):
    def eat(self, decrease):
        self.hunger -= decrease
        print('{} is eating, hungers is decreasing'.format(self.name))

    def behavior(self):
        pass


class Predator(AnimalKingdom):
    def eat(self, decrease):
        self.hunger -= decrease
        print('{} is eating, hungers is decreasing'.format(self.name))

    def behavior(self):
        pass


class Amphibian(AnimalKingdom):
    def eat(self, decrease):
        self.hunger -= decrease
        print('{} is eating, hungers is decreasing'.format(self.name))

    def behavior(self):
        pass


Elephant = Mammals('Elephant')
print(Elephant.name)
Elephant.eat(20)
