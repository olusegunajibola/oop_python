# Single Inheritance
class GrandMother:
    def __init__(self, gName) -> None:
        self.gName = gName

    def getGName(self):
        print("GrandMother's name is: ", self.gName)


class Mother(GrandMother):
    def __init__(self, mName, gName) -> None:
        self.mName = mName
        super().__init__(gName)

    def getMName(self):
        print("Mother's name is: ", self.mName)


class You(Mother):
    def __init__(self, name, mName, gName) -> None:
        self.name = name;
        super().__init__(mName, gName)

    def getName(self):
        print("Your name is: ", self.name)


y1 = You('Bob', 'Tina', 'Sam')

y1.getName()
y1.getMName()
y1.getGName()