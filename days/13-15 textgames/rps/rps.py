'''
Classes
Roll

    name of roll
    rolls that can be defeated by self
    rolls that defeated self

Player

    name of player
'''
import random
from rps_actors import Player, Roll

def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name, 0)
    player2 = Player("computer", 0)

    game_loop(player1, player2, rolls)

def print_header():
    print('------------------------------------------')
    print('         Rock, Paper, Scissors!')
    print('------------------------------------------')
    print()

def get_players_name():
    cmd = input("Player 1, please enter your name: ")
    print()
    return cmd

def build_the_three_rolls():
    rolls = [
        Roll('Scissors'), 
        Roll('Rock'),
        Roll('Paper') 
    ]
    return rolls

def game_loop(player1, player2, rolls):

    while True:
        p2_roll = random.choice(rolls)
        while True:
            p1_roll = input('Select your roll: [r]ock, [p]aper, or [s]cissors? ')
            if p1_roll == 'r':
                p1_roll = rolls[1]
                break
            elif p1_roll == 'p':
                p1_roll = rolls[2]
                break
            elif p1_roll == 's':
                p1_roll = rolls[0]
                break
            else:
                print("Please enter a valid roll.")
                print()

        outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        print('You throw {}, {} throws {}.'.format(
            p1_roll.roll, player2.name, p2_roll.roll
        ))

        # display winner for this round        
        if outcome == p1_roll.get_name():
            print("{} wins!".format(player1.name))
            player1.score += 1
        elif outcome == p2_roll.get_name(): 
            print("{} wins!".format(player2.name))
            player2.score += 1
        else:
            print(outcome)
        
        print()
        
        # Compute who won
        if player1.score >= 2:
            print("{} defeated {}.".format(
                player1.name, player2.name
            ))
            break
        elif player2.score >= 2:
            print("{} defeated {}.".format(
                player2.name, player1.name
            ))
            break
    False

    print()


if __name__ == '__main__':
    main()
