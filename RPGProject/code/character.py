## Character Class
# Meant to have a personality, but not to have specific combat abilities
from creature import Creature

class Character(Creature):

  def __init__(self, Id, Name, Category, Size, Senses, Challenge, Moves, Vulnerabilities,
                 Resistances, Immunities, AC, HealthMax, Strength, Dexterity, Constitution, Intelligence,
                 Perception, Charisma, Speed, SwimSpeed, FlySpeed, SpecialAbilities, Behavior, Languages,
                 Region,X,Y,Personality,Ethnicity):
    super().__init__(Id, Name, Category, Size, Senses, Challenge, Moves, Vulnerabilities,
                 Resistances, Immunities, AC, HealthMax, Strength, Dexterity, Constitution, Intelligence,
                 Perception, Charisma, Speed, SwimSpeed, FlySpeed, SpecialAbilities, Behavior, Languages,
                 Region,X,Y)
    this.Personality = Personality
    this.Ethnicity = Ethnicity

def Default():
  return Character(1, "Creature", 1, 3, [], 1, [], [], [], [], 11, 20, 1, 2, 3, 4, 5, 6, 30.0, 10.0, 0.0, [], 1, [], 1, 2, 2, 0, 0)
