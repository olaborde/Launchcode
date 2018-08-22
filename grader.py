# Dictionaries

person_1 = {
  'occupation' : 'Web Developer',
  'name' : 'John Smith',
  'gender' : 'male',
  'age' : 65,
  'books' : ['harry potter'],

  'attributes' : {

  },

  'hungry' : True

}

print(person_1)

person_1['height'] = 8.5

print(person_1)

class_1 ={
  'students' : 50,
  'Instructor' : 10
}


# Loops through

# for a,b in dictio:
# for key,value in dictio:

# .keys() --- return the list of keys

# .values() --- return list of values

# .get(x,y) ----- Gets the value at key x, otherwise return y

# del variable[key] --- to delete

person_2 = {
  'occupation' : 'Web Developer',
  'name' : 'John Smith',
  'gender' : 'male',
  'age' : 65,
  'books' : ['harry potter'],

  'attributes' : {
    'height' : 4.5,
    'weight' : 180,
    'hair_color' : 'Brown'

  },

  'hungry' : True

}


print(person_2.get('likes', 'no likes found') )

print(person_2['attributes']['hair_color'])

person_2['likes'] = ['walks on the beach', ' running', 'weight lifting']
print(person_2.get('likes', 'no likes found') )

