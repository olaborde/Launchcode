def initials():
    name = input( "What is your name?")
    return .join("")([ name[0] for name in fullname.split(" ")]).upper()