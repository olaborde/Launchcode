import string

def alphabet_position(letter):
  new_letter = letter.lower()
  a_z = list(string.ascii_lowercase)
    
  for position, i in enumerate(a_z):
    if i == new_letter:
      return position


# rotate_character
def rotate_character(char, rot):
  #list of string
  a_z = list(string.ascii_lowercase)
  # Grab the position of the character to add to rot
  if str(char).isalpha():
    new_char = alphabet_position(char)
    the_char =( new_char + rot ) % 26
    if char.isupper():
      return (a_z[the_char].upper())
    else:
      return (a_z[the_char])  
  else:
    
    return char   