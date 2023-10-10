class Employee:
    # Class variables
    companyName = 'Python Developers'
    'Common base class for all employees'
    empCount = 0

    # Constructor
    def __init__(self, *args):
        if len(args) < 5:
            self.id = 1000
            self.firstName = 'Unknown'
            self.lastName = 'Unknown'
            self.age = 'Unknown'
            self.salary = 0
            Employee.empCount += 1
        else:
            self.id = args[0]
            self.firstName = args[1]
            self.lastName = args[2]
            self.age = args[3]
            self.salary = args[4]
            Employee.empCount += 1
    # def __init__(self, name, salary):
    #     self.name = name
    #     self.salary = salary
    #     Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print('Employee ID: ', self.id,
              "\nFirst Name: ", self.firstName,
              "\nLast Name: ", self.lastName,
              "\nAge: ", self.age,
              "\nSalary: ", self.salary)


"This would create first object of Employee class"
emp1 = Employee(1234, "Zara", "Gucci", 23, 20000)
"This would create second object of Employee class"
# emp2 = Employee("Manni", 5000)

# emp1.age = 7  # Add an 'age' attribute.
# emp1.age = 8  # Modify 'age' attribute.

emp1.displayEmployee()
# print(emp1.age)
# emp2.displayEmployee()
# # Employee.__hasattr__(emp1, 'age')
# print(hasattr(emp1, 'age'))  # Returns true if 'age' attribute exists
# print(getattr(emp1, 'age') )   # Returns value of 'age' attribute
# print(setattr(emp1, 'age', 9)) # Set attribute 'age' at 9
# print(getattr(emp1, 'age') )
# delattr(empl, 'age'))    # Delete attribute 'age'
print("Total Employee: %d" % Employee.empCount)