def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    new_fullname = fullname
    initials = ''
    fullname = fullname.split(' ') 
    for i in range(len(fullname)):
        initials += fullname[i][0].upper()
    print('The initials of '+ new_fullname + ', are '+ initials)




def main():
# some more code here (input and print statements)
    fullname = input('What is your name:')
 
    get_initials(fullname)

if __name__ == '__main__':
    main()