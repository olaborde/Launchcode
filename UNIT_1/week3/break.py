from random import shuffle

marbles = [
  {'color':'red'},
  {'color':'red'},
  {'color':'red'},
  {'color':'red'},
  {'color':'red'},
  {'color':'red'},
  {'color':'red'},
  {'color':'red'},
  {'color':'blue'},
  {'color':'red'},
  {'color':'red'},
]


shuffle(marbles)


count = 0

for marble in marbles:
  if marble['color'] == 'blue':
    break
  else:
    print('.')
    count += 1

print("You counted", count, "before arriving to the to blue model")    

