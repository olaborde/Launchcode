# tuples

bob = ('bob', 40, 'Male', 'Miami')
print(bob)
# modifiy the tuple  
bob = bob[:2] + ('female',) + bob[:3]

print(bob)

print(list(bob))