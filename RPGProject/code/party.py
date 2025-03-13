# Party Class
# An adventuring/questing party, contains characters and sets up their roles
import character

class Party:

  def __init__(self, members, allies, enemies, leader):
    self.members = members
    self.allies = allies
    self.enemies = enemies
    self.leader = leader

def default():
  cha = character.default()
  return Party([cha.id],[],[],cha.id)
