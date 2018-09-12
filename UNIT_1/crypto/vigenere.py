

from helpers import alphabet_position, rotate_character

def encrypt(text, key):
  non_alpha = 0
  final_text = ""
  breakdown_key = []

  #for y in range(len(text)):
  for i in key:
   
    key_position = alphabet_position(i)
    
    breakdown_key.append(key_position)

  for item in range(len(text)): 

    if text[item].isalpha(): 
      # for j in text:
      x = (item - non_alpha) % len(breakdown_key)
        
      new_char = rotate_character(text[item], breakdown_key[x])
      final_text = final_text + new_char
      # return final_text

    else:
      non_alpha = non_alpha + 1 
      final_text = final_text + text[item]  

  return final_text   


def main():
    itext = input("Please, type a message:")                   
    ikey = input("Please, enter an encryption key:")         
    print(encrypt(itext, ikey))  
                                                

if __name__ == '__main__':
    main()

