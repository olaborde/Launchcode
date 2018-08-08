

# Nested Loops


for n in range(3):
  for x in range(2):
    print('Hip')
  print("Hooray") 



group_of_names =[
  ['joe','lou','blake'],
    ['max', 'peter', 'charles'],
    ['Zack','Bibi', 'boo']
  ]

for names in group_of_names:
  for name in names:
    print(name)
print(group_of_names[1][1])    


g_of_names =[
  ['joe','lou','blake'],
    ['max', 'peter', 'charles'],
    ['Zack','Bibi', 'boo']
  ]

num_of_letters = 0

for group in g_of_names:
  for name in group:
    if len( name ) > num_of_letters:
      num_of_letters = len( name)


print('THe largest name in your list is', name, "it has ", num_of_letters)


def divisible_by_eleven(start_num, end_num):
  for num in range(start_num, end_num):
    if num % 11 == 0:
      print('Found it:', num)
      break #found the first one
    print('.')  

divisible_by_eleven(1935, 2018)   


