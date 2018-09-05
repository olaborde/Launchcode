import string

def alphabet_position(letter):
  new_letter = letter.lower()
  a_z = list(string.ascii_lowercase)
    
  for position, i in enumerate(a_z):
    if i == new_letter:
      return position
