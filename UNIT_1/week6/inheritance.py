class Animal:
      def __init__(self, color, breed, legs, name):
    self.color = color
    self.breed = breed
    self.legs = int(legs)
    self.name = name


class Mamal( Animal ):
  def __init__(self, color, breed, name, furLen):
    Animal.__init__(self, color, breed, 4, name)
    self.furLen = furLen



fido = Mamal("Black", "Labrador","Fido", "long")

maxine = Animal("Black", "Labrador",4, "Maxine")



print(fido.breed)
print(fido.color)
print(fido.legs)
print(fido.name)
print(fido.furLen) #AttributeError: 'Animal' object has no attribute 'furLen'


print("--------")

print(maxine.breed)
print(maxine.color)
print(maxine.legs)
print(maxine.name)
print(maxine.furLen) #AttributeError: 'Animal' object has no attribute 'furLen'