

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


    def eat(self):
        return self.hungry = False

    def sleep(self):
        self.tired = False
        self.hungry = True

    def run(self):
        self.tired = True       