# composition is to represent that a class can have a relationship
class Car:
    def __init__(self, name, engine, owner):
        self.name = name
        self.engine = engine
        self.owner = owner
        self.detail = name + ' ' + engine + ' ' + owner

class Person:
    def __init__(self, name):
        self.name = name


sami = Person('sami')
ferrari = Car('Ferrari', 'V8', sami.name)

print(ferrari.detail)
