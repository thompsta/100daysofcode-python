import random

# classes are blueprints of the objects we want to create
# every method has the __init__ self, assign new fields (characteristics) with self
class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    # add new behaviors (methods) with new functions within the class
    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self.level 

# pass the Creature class as parameter so that you can inherit Creature characteristics
class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        # use super() to reference Creature characteristics
        super().__init__(name, level)
        # storing additional characteristics
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def defensive_roll(self):
        # can also use super() to call methods from Creature class
        roll = super().defensive_roll()
        value = roll * self.scaliness
        if self.breaths_fire:
            value = value * 2

        return value

class Wizard(Creature):

    def attack(self, creature):
        my_roll = self.defensive_roll()
        their_roll = creature.defensive_roll()

        return my_roll >= their_roll

    
