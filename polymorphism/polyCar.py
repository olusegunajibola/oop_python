class Car:

    def carChar(self, *args):
        if len(args) == 0:
            print("Color = none")
            print("Type = unknown")
        elif len(args) == 1:
            print("Color = ", args[0])
            print("Type = unknown")
        elif len(args) == 2:
            print("Color = ", args[0])
            print("Type = ", args[1])


c1 = Car()
c1.carChar()
print()
c1.carChar('Blue')
print()
c1.carChar('Red', 'Ford')


# alternative is below:
# but this is not allowed in Python. Hence, the above is better.

# class Car:
#     def carChar(self):
#         print("Color = none")
#         print("Type = unknown")
#
#     def carChar(self, color):
#         print("Color =", color)
#         print("Type = unknown")
#
#     def carchar(self, color, types):
#         print("Color = ", color)
#         print("Type = ", types)
#
#
# c1 = Car()
#
# c1.carChar()
# c1.carChar('Blue')
# c1.carchar('Red', 'Ford')
