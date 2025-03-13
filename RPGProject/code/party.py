# Party Class
# An adventuring/questing party, contains characters and sets up their roles
import character

class Party:

  def __init__(self, id, members, allies, enemies, leader):
    self.Members = members
    self.Allies = allies
    self.Enemies = enemies
    self.Leader = leader
    self.Id = Id

def Default():
  cha = character.Default()
  return Party(1,[cha.Id],[],[],cha.Id)
