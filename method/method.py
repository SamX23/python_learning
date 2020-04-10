# https://julien.danjou.info/guide-python-static-class-abstract-methods/
class Vegetable:
    protein = 100

    def __init__(self, name, vitamin):
        self.name = name
        self.vitamin = vitamin
        self.cheese = 10
        self.milk = 10

    def get_name(self):
        return self.name

    def get_vitamin(self):
        return self.vitamin

    # method that does not use object class at all
    @staticmethod
    def mix(x, y):
        return x + y

    def cook(self):
        return self.mix(self.cheese, self.milk)

    # class method that a method is bound to the class itself
    @classmethod
    def get_protein(cls):
        return cls.protein

    def get_cheese(self):
        return self.cheese

    def get_milk(self):
        return self.milk

    @classmethod
    def mix_vitamin(cls, healhty):
        return cls(healhty.get_cheese() + healhty.get_milk())


wortel = Vegetable('Wortel', 'A')
bayam = Vegetable('Bayam', 'B')
print(wortel.get_name)
print(wortel.get_name())
print(Vegetable.get_name(wortel))
print(Vegetable('Bayam', "B").get_vitamin)
print(Vegetable('Bayam', "B").get_vitamin())
print(Vegetable.get_vitamin(wortel))
print(bayam.cook())
print(wortel.get_protein())
