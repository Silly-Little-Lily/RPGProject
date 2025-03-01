## Creature Class

class Creature:

    def __init__(self, Id, Name, Category, Size, Senses, Challenge, Moves, Vulnerabilities,
                 Resistances, Immunities, AC, HealthMax, Strength, Dexterity, Constitution, Intelligence,
                 Perception, Charisma, Speed, SwimSpeed, FlySpeed, SpecialAbilities, Behavior, Languages,
                 Region,X,Y):
        self.Id = Id
        self.Name = Name
        self.Category = Category
        self.Size = Size
        self.Senses = Senses
        self.Challenge = Challenge
        self.Moves = Moves
        self.Vulnerabilities = Vulnerabilities
        self.Resistances = Resistances
        self.Immunities = Immunities
        self.AC = AC
        self.HealthMax = HealthMax
        self.Strength = Strength
        self.Dexterity = Dexterity
        self.Constitution = Constitution
        self.Intelligence = Intelligence
        self.Perception = Perception
        self.Charisma = Charisma
        self.Speed = Speed
        self.SwimSpeed = SwimSpeed
        self.FlySpeed = FlySpeed
        self.SpecialAbilities = SpecialAbilities
        self.Behavior = Behavior
        self.Languages = Languages
        self.Conditions = []
        self.HP = HealthMax
        self.State = 1
        self.Region = Region
        self.X = X
        self.Y = Y
        self.AnimationCycle = 1

def Default():
  return Creature(1, "Creature", 1, 3, [], 1, [], [], [], [], 11, 20, 1, 2, 3, 4, 5, 6, 30.0, 10.0, 0.0, [], 1, [], 1, 2, 2)
