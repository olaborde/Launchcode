def analyze_text(text):
    new_text = text.lower()
    print(new_text)
    input_text = new_text.replace(" ", "")
    print(input_text)
    print(type(input_text))
    for char in input_text:
        if char.isalpha():
            found_e = int(input_text.count('e') + input_text.count('E') )
            text_length = len(input_text) 

            percentage_of_e = (found_e / text_length) * 100
    # else:
    #   print('Please enter only letters or sentence')  
    # analyze_text()


    print( f'' The text contains, {text_length}, alphabetic characters, of which, {found_e}, ( {percentage_of_e} )%, are '')

    # print('The text contains', text_length, 'alphabetic characters','of which', found_e,'(',percentage_of_e,')','%', ''' are 'e' ''')


text1 = "Eeeee"
answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."


text2 = "Blueberries are tasteee!"
answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."


text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."


# Tests 4-6: solutions using str.format should pass these
text4 = "Eeeee"
answer4 = "The text contains 5 alphabetic characters, of which 5 (100%) are 'e'."


text5 = "Blueberries are tasteee!"
answer5 = "The text contains 21 alphabetic characters, of which 7 (33.33333333333333%) are 'e'."


text6 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer6 = "The text contains 55 alphabetic characters, of which 0 (0%) are 'e'."


analyze_text(text1)
analyze_text(text2)
analyze_text(text3)
# analyze_text(text4)
# analyze_text(text5)
# analyze_text(text6)