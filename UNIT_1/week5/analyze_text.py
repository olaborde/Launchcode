def analyze_text(text):
      count = 0
  e_count = 0
  for letter in text:
    if letter == 'E' or letter == 'e':
      e_count += 1
    if letter.isalpha():
      count += 1
  return " The text contains  {} alphabetic characters, of which {} ({}%) are 'e'.".format(count, e_count, (e_count/count*100))      




print(analyze_text('Eeeee')  )