class Team:
      def __init__(self, name, player1, player2, player3, player4):
    self.name = name
    self.player1 = player1
    self.player2 = player2
    self.player3 = player3
    self.player4 = player4

  def getName(self):
    return self.name


  def setName(self, newName):
    self.name = newName
    return "" 


myTeam = Team( "GreenTeam", "Bob", "James", "Marie", "John")


print(myTeam.getName())


newName = myTeam.setName("RedTeam")

print(myTeam.getName())



 


