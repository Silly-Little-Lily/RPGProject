# Party Class
# An adventuring/questing party, contains characters and sets up their roles

class Party:

  def __init__(self, members, allies, enemies, leader):
    self.members = members
    self.allies = allies
    self.enemies = enemies
    self.leader = leader
