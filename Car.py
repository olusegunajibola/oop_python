class car:

  def __init__(self, year, speed): #There are 2'_' on each side
    self.year = year
    self.speed = speed

  def getSpeed(self):
    print("Speed: ", self.speed)
  def setSpeed(self, speed):
    self.speed = speed
  def getYear(self):
    print("Year: ", self.year)
  def setYear(self, year):
    self.year = year

Ford = car(2021, 130)
Chevy = car(2019, 110)

#car.getSpeed(Ford) #Both are common practice in calling
Ford.getSpeed() # the function
Chevy.getSpeed()
Ford.setSpeed(120) #Changing the object values
Ford.getSpeed()
Ford.getYear()