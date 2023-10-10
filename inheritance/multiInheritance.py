#Mother and her parents
class MGrandMother:
  def __init__(self, mgmName) -> None:
      self.mgmName = mgmName
  def getMGMName(self):
    print("GrandMother's name is: ", self.mgmName)

class MGrandFather:
  def __init__(self, mgfName) -> None:
      self.mgfName = mgfName
  def getMGFName(self):
      print("GrandFather's name is: ", self.mgfName)

class Mother(MGrandMother, MGrandFather):
  def __init__(self, mName, mgmName, mgfName) -> None:
      self.mName = mName
      MGrandMother.__init__(self, mgmName)
      MGrandFather.__init__(self, mgfName)
  def getMName(self):
      print("Mother's name is: ", self.mName)

#Dad and his parents
class DGrandMother:
  def __init__(self, dgmName) -> None:
      self.dgmName = dgmName
  def getDGMName(self):
    print("Dad's GrandMother's name is: ", self.dgmName)

class DGrandFather:
  def __init__(self, dgfName) -> None:
      self.dgfName = dgfName
  def getDGFName(self):
      print("Dad's GrandFather's name is: ", self.dgfName)

class Father(DGrandMother, DGrandFather):
  def __init__(self, dName, dgmName, dgfName) -> None:
      self.dName = dName
      DGrandFather.__init__(self, dgfName)
      DGrandMother.__init__(self, dgmName)
  def getDName(self):
      print("Father's name is: ", self.dName)

class You(Mother, Father):
  def __init__(self, name, mName, mgmName, mgfName,  dName, dgfName, dgmName) -> None:
      self.name = name;
      Mother.__init__(self, mName, mgmName, mgfName)
      Father.__init__(self, dName, dgmName, dgfName)
  def getName(self):
      print("Your name is: ", self.name)


y1 = You('Bob', 'Tina', 'Samantha', 'John', 'Nick', 'Tim', 'Sandy')


y1.getName()
y1.getMName()
y1.getMGMName()
y1.getMGFName()
y1.getDName()
y1.getDGFName()
y1.getDGMName()