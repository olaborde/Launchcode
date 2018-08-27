

#   def start(self)   
#---------------------------------- Properties (parameters)
#                     |    |      |
#                     v    v      v
class Person:
  def __init__(self, name, gndr, occp):
    # variable ---
    #            |
    #            V 
    self.name = name  
    self.gender = gndr
    self.occupation = occp

  def greet(self):
    return "Hello, my name is " + self.name  

  def greet_person(self, otherName):
    return "Hello, " + otherName + " my name is "  + self.name  

mark = Person( "Mark", "Male", "Surgeon" ) 
suzie = Person( "Suzie", "Female", "Lawyer" ) 

print(mark.gender)
print(mark.name)  # properties   

print(mark.greet())  # methods
print(suzie.greet_person(mark.name))  # methods 