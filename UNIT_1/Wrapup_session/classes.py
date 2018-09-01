

# classes are blueprint of what an object should


class Person:
    
    def __init__(self, name, gender, age, height, weight, race, eyecolor, haircolor = "black"):
        # required - unique
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.race = race
        self.eyecolor = eyecolor
        self.haircolor = haircolor
        self.hungry = True
        self.tired = True

        # required
        self.alive = True
        self.legs = 2
        self.arms = 2


    def walk(self):
        return self.name + "walks forward"   


    def say(self, sentence):
        return self.name + "Says" + sentence 

    def greet(self, human):
        return "Hello " + human.name + " My name is " + self.name  


    def eat(self):
        print("jjj")
        return self.hungry
        # return self.hungry = False

    def sleep(self):
        self.tired = False
        self.hungry = True

    #  mutator function
    def run(self):
        self.tired = True

    def __repr__(self):
        return "Hi, I am {}, I am {} year old {} {}, I'm {} ft tall".format(self.name, self.age, self.race, self.gender, self.height)      


person_1 = Person("Sally", "Female", 30, 4.2, 100, "ASian", "Green", "Brown")    

person_2 = Person("Pete", "Male", 30,100, "Black", "Green", "Brown")   
person_3 = Person("Bryan", "Female", 25, 100, "Italian", "Blue", "Red")  

print( person_1)

print( person_1.greet(person_2))