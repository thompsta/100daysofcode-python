import random

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
class Roll():
    def __init__(self, roll): 
        self.roll = roll
        
    def get_name(self):
        return self.roll

    def can_defeat(self, beats):
        # rolls that can be defeated by self  
        my_roll = self.get_name()
        their_roll = beats.get_name()
        if my_roll in 'Rock' and their_roll in 'Scissors':
            winner = my_roll
        elif my_roll in 'Scissors' and their_roll in 'Paper':
            winner = my_roll
        elif my_roll in 'Paper' and their_roll in 'Rock':
            winner = my_roll
        elif my_roll == their_roll:
            winner = "Tie game!"
        else:
            winner = their_roll
        return winner

    
