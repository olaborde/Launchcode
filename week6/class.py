class Person:
  def __init__(self, name, gndr, occp):
    # variable ---
    #            |
    self.name = name  
    self.gender = gndr
    self.occupation = occp

mark = Person( "Mark", "Male", "Surgeon" ) 

print(mark.gender)
print(mark.name)   