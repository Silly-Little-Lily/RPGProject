## Species Class

class Species:

    def __init__(self, Id, Name, NamePlural, Category, Size, Senses, Challenge, Moves, Vulnerabilities,
                 Resistances, Immunities, AC, HP, Strength, Dexterity, Constitution, Intelligence,
                 Perception, Charisma, Speed, SwimSpeed, FlySpeed, SpecialAbilities, Behavior, Languages):
        self.Id = Id
        self.Name = Name
        self.NamePlural = NamePlural
        self.Category = Category
        self.Size = Size
        self.Senses = Senses
        self.Challenge = Challenge
        self.Moves = Moves
        self.Vulnerabilities = Vulnerabilities
        self.Resistances = Resistances
        self.Immunities = Immunities
        self.AC = AC
        self.HP = HP
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

def Default():
    return Species(1,"Species","Species",1,3,[1],12,[2],[3],[4],[5],11,"2d6+2",1,2,3,4,5,6,30.0,10.0,0.0,[1],2,[1])
