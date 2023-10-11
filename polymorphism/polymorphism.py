# Abstract Method
class Fruit:
    def caleries(self):
        raise NotImplementedError('Please use caleries in your method')


class Apple(Fruit):
    def caleries(self):
        print("Apple has 95 caleries")


class Orange(Fruit):
    def caleries(self):
        print("Orange has 45 caleries")


class Banana(Fruit):
    def caleries(self):
        print("Banana has 105 caleries")


def FruitCal(cal):
    cal.caleries()


a1 = Apple()
b1 = Banana()
o1 = Orange()

FruitCal(a1)
FruitCal(b1)
FruitCal(o1)
