
def analyze_text(text):
  new_char = ''
  new_text = text.lower()
  input_text = new_text.replace(" ", "") 
  the_text = list(input_text)
  for char in the_text:
    if char.isalpha():
      new_char += char
  text_length = len(new_char)
  found_e = new_char.count('e') 
  percentage_of_e = (found_e / text_length) * 100
  return """The text contains {} alphabetic characters, of which {} ({}%) are 'e'.""".format(text_length, found_e, percentage_of_e)



analyze_text('Eeeee')