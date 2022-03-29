# https://www.codecademy.com/courses/learn-intermediate-python-3/projects/python-school-catalogue
# Q1 Q2 Q3 Q4 Q5 Q6
class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def __repr__(self):
    return "A {level} school named {name} with {numberOfStudents} students".format(level=self.level, name=self.name, numberOfStudents=str(self.numberOfStudents))

  
  def getName(self):
    return self.name
  def getLevel(self):
    return self.level
  def getNumberOfStudents(self):
    return self.numberOfStudents  
  def setNumberOfStudents(self, numStudent):
    self.numberOfStudents = numStudent


# Q8 Q9 Q10 
class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy
  
  def getPickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + ". The pickup polity is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

# Q15 
class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams
  
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + ". Lists of sport teams available:\n{sportsTeams}".format(sportsTeams = '\n'.join(self.sportsTeams))
  
  def getSportsTeams(self):
    return self.sportsTeams

# Q7
mySchool = School("Codecademy", "high", 100)
print(mySchool)
print(mySchool.getName())
print(mySchool.getLevel())
mySchool.setNumberOfStudents(200)
print(mySchool.getNumberOfStudents())
print(mySchool)
print("\n")

# Q14
testSchool = PrimarySchool("Codecademy Primary", 300, "Pickup Allowed")
print(testSchool.getPickupPolicy())
print(testSchool)
print("\n")

# Q16
c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.getSportsTeams())
print(c)