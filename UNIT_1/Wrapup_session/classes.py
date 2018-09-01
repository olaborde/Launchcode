

# classes are blueprint of what an object should


class Person:
    
    def __init__(self, name, gender, age, height, weight, race, eyecolor, haircolor):
        # required - unique
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.race = race
        self.eyecolor = eyecolor
        self.haircolor = haircolor

        # required
        self.alive = True
        self.legs = 2
        self.arms = 2
