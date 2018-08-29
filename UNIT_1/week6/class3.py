class Team:
      def __init__(self, player1, player2, player3, player4):
    self.player1 = player1
    self.player2 = player2
    self.player3 = player3
    self.player4 = player4


  def getPlayers(self):
    return [self.player1, self.player2, self.player3, self.player4]

  def __repr__(self):
    return " I am a team of: {}, {}, {}, {}".format(self.player1, self.player2, self.player3, self.player4)  


  def __len__(self):
    return len(self.getPlayers())  


  def __contains__(self, player):
    return player in self.getPlayers()  
    
    
    
myTeam = Team("Bob", "Mary", "James", "Joan")

print(myTeam)

# print( myTeam.getPlayers())

print(len(myTeam))

print( "Bob" in myTeam)

