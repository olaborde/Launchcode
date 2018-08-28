counts = dict()

names = ['csev','cwen', 'csev', 'zqien', 'cwen']

for name in names:
  if name not in counts:
    counts[name] = 1
  else:
    counts[name] = counts[name] + 1
print(counts)      


places = ['Miami', 'Tokyo', 'Paris', 'New York', 'Sao Polo', 'Miami', 'Paris', 'Tokyo']

for place in places:
  print(place)

# if places in counts:
#   x = counts[places]
# else:
#   x = 0
#   x = counts.get(places, 0)  
# print(counts)  