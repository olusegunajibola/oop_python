class BankAccount:
    # Overloading is not allowed
    #  def __init__(self):
    #    self.name = "Unknown"
    #    self.accountNumber = 1234
    #    self.balance = 0

    #  def __init__(self, name, accountNumber, balance):
    #      self.name = args[0]
    #      self.accountNumber = args[1]
    #      self.balance = args[2]

    # Class Attributes
    name = ""
    accountNumber = 0
    balance = 0

    def __init__(self, *args):
        if len(args) < 3:  # Data Attribute
            self.name = "Unknown"
            self.accountNumber = 1234
            self.balance = 0
        else:
            self.name = args[0]
            self.accountNumber = args[1]
            self.balance = args[2]

    def getName(self):
        return self.name

    def getAcctNum(self):
        return self.accountNumber

    def getBalance(self):
        return self.balance

    def setName(self, name):
        self.name = name

    def setBalance(self, balance):
        self.balance = balance

    def setAcctNum(self, accountNumber):
        self.accountNumber = accountNumber

    def deposit(self, balance):
        self.balance += balance

    def withdraw(self, balance):
        self.balance -= balance

    def toString(self):
        print("Name: " + self.name + "\nAccount Number: "
              + str(self.accountNumber)
              + "\nBalance: $" + str(self.balance))


Bob = BankAccount()
Tim = BankAccount("Tim", 10012, 1200)
Bob.toString()
print()
Tim.toString()
print()
Tim.name