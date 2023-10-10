import math

class Student:
    # first_name =
    # last_name =
    # gender =
    # year =
    __yearClass = {1: 'first-year student', 2: 'sophomore',
                   3: 'junior', 4: 'senior'}
    yearClass = {1: 'first-year student', 2: 'sophomore',
                 3: 'junior', 4: 'senior'}

    # gpa =

    def __init__(self, first_name, last_name, gender, year, gpa):
        assert isinstance(year, int), "input integer"
        assert gender == 'M' or gender == 'F'

        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.year = self.__yearClass.get(year)
        self.gpa = gpa

    def student_study_time(self, study_time):
        self.gpa += math.log(study_time, 10)
        if self.gpa > 4.0:
            self.gpa = 4.0

    def show_student(self):
        print("first name: ", self.first_name,
              "\nlast name: ", self.last_name,
              "\ngender: ", self.gender,
              "\nyear: ", self.year,
              "\ngpa: ", self.gpa
              )


std1 = Student("Adam", "Bond", "M", 1, 3)
std1.student_study_time(30)
std2 = Student("Eric", "Lev", "M", 2, 1.2)
std2.student_study_time(60)
std3 = Student("Judie", "Rose", "F", 3, 3.8)
std3.student_study_time(90)
std4 = Student("Barbara", "Tim", "F", 4, 3.7)
std4.student_study_time(120)
std5 = Student("Elvis", "Wayne", "M", 4, 1.1)
std5.student_study_time(180)

student_GPA = [std1, std2, std3, std4, std5]

for std in student_GPA:
    std.show_student()
    print()

# std1.show_student()
# print(std1.gpa)
# print(Student.yearClass)
# print(Student.__yearClass) # error because user cannot access or modify
