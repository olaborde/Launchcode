counter = [1, 2, 3, 4]

text = "supercalifragilisticexpialidocious"

'''
    s
    ss
    sss
    ssss
    u
    uu
    uuu
    uuuu
    p
    pp
    ppp
    pppp
'''

for letter in text:
    for num in counter:
        print(letter * num)


def sendMessage(number, message ):
    print('Sending: {} to {}'.format(message, number))

PhoneNumbers = ['305-322-2311', '999-322-2211', '767-322-2211', '883-322-2211', '305-878-088']

messages = ['Hello there',
            'Brunch tommorow',
            'Invite to my party',
            'RSVP training session'
]


counter = 0

for theNumber in PhoneNumbers:
    sendMessage( theNumber, messages[counter])

    if counter < (len( messages ) - 1):
        counter += 1
    else:
        counter = 0    

# for theNumber in PhoneNumbers:
#     for theMessage in messages:
#         print( theNumber, theMessage)






