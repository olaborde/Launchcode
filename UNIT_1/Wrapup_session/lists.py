

def list_my_fruits( myItems ):

    counter = 1

    for items in myItems:
        print ( counter, items)
        counter += 1


myRefrigirator = [ 'Banana', 'Mangoes', 'Strawberries' ] 


list_my_fruits( myRefrigirator )

userInput = ''
while userInput.lower() != 'done':
    userInput = input("What fruit would you like to add: ")
    if userInput.lower() != 'done':
        print( "Adding {} to my refrigirator".format(userInput))
        myRefrigirator.append( userInput )
list_my_fruits( myRefrigirator )        





# ask user to add fruit
# take the user input
#Add to list
# ask again
# if user typles "Done"
# List all the fruits they have