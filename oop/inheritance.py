# inheritance is to inherit attributes
# from main class to submain class
class Car():
    def __init__(self, engine, transmission, fuel):
        self.engine = engine
        self.transmisssion = transmission
        self.fuel = fuel
    
    def cetak(self):
        print(self.engine)

    def cetakAll(self):
        print(self.engine)
        print(self.transmisssion)
        print(self.fuel)

avanza = Car('VVTI', 'M/T', 'Premium')
avanza.cetak()
print(avanza.fuel)
print(avanza.transmisssion)
print()

# Sport class is inherrit from Car class, Sport class
# can use variables and method of Car class.
class Sport(Car):
    # define new method
    def track(self, place):
        print('This car is for {}'.format(place))
    
    def speed(self, speed):
        print('The max speed is {} km/h'.format(speed))
        pass

subaru = Sport('Boxer', 'M/T', 'Pertamax')
subaru.cetakAll()
subaru.track('Racing')
subaru.speed(250)


        