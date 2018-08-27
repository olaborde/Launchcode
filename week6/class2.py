class Car:
      def __init__(self, theBrand, theColor, numDoors):
    self.engineOn = False
    self.brand = theBrand
    self.color = theColor
    self.doors = numDoors
    self.position = 0

  def details(self):
    return self.brand, self.color, self.doors  

  # allow to return object return
  def __repr__(self):
  
    return "This is a "+ self.color+" "+self.brand+ " with " + str(self.doors)+ " doors" 

  def startEngine(self):
    self.engineOn = True
    print("Vroooom!")

  def move(self, meters):
    self.position += meters
    print("The "+ self.brand+ " moved "+ str(self.position)+ " meters")



myFirstCar = Car('Lexus', "Black", 4)    

# print(myFirstCar.details())


print(myFirstCar)
print(myFirstCar.engineOn)
myFirstCar.startEngine()
print(myFirstCar.engineOn)

print(myFirstCar.move( 20 ))

print(myFirstCar.position)