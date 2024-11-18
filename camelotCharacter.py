"""Marianne Adams
CS120
Path to Camelot
Character Module"""

class Character(object):
    def __init__(self, name = "Billy Bob John", hitPoints = 10, hitChance = 30, maxDamage = 3, healingFactor = 20, maxHealing = 4, armor = 0):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.healingFactor = healingFactor
        self.maxHealing = maxHealing
        self.armor = armor
        
    def testInt(self, value, min = 0, max = 100, default = 0):
        