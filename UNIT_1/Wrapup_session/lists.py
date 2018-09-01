

def list_my_fruits( myItems ):

    counter = 1

    for items in myFruitsLists:
        print ( counter, items)
        counter += 1


myFruitsLists = [ 'Banana', 'Mangoes', 'Strawberries' ] 


list_my_fruits( myFruitsLists )



# add more items to the lists

myFruitsLists.append( ' Coconuts ')  
myFruitsLists.append( ' Kiwi ')     
list_my_fruits( myFruitsLists )