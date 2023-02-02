'''
Card Game Interface
'''

import os
import random
import time

class Cards:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.values = {'1': 1,
                       '2': 2, 
                       '3': 3, 
                       '4': 4,
                       '5': 5, 
                       '6': 6, 
                       '7': 7, 
                       '8': 8, 
                       '9': 9, 
                       '10': 10, 
                       'Jack': 11, 
                       'Queen': 12, 
                       'King': 13, 
                       'Ace': 14}
        self.picked_cards = set()

    def random_card(self):
        self.random_suit = random.choice(self.suits)
        self.random_value = random.choice(sorted(self.values))
        card_picked = self.random_value + ' of ' + self.random_suit
        while card_picked in self.picked_cards:
            self.random_suit = random.choice(self.suits)
            self.random_value = random.choice(sorted(self.values))
            card_picked = self.random_value + ' of ' + self.random_suit
        self.picked_cards.add(card_picked)
        return card_picked


class Games:
    def __init__(self):
        self.player_1_value = 0
        self.player_1_score = 0
        self.player_2_value = 0
        self.player_2_score = 0


    def check_winner():
        if game.player_1_score > game.player_2_score:
            print(f'Player 1 was won with a score of {game.player_1_score}')
        elif game.player_2_score > game.player_1_score:
            print(f'Player 2 has won with a score of {game.player_2_score}')
        elif game.player_1_score == game.player_2_score:
            print('Both players have tied')
        else:
            return False

    def war(self):
        time.sleep(1)
        while len(cards.picked_cards) != 52:
            player_1_card = cards.random_card()
            game.player_1_value = cards.values.get(cards.random_value)
            print(f'Player 1 drew {player_1_card}')
            # time.sleep(1)

            player_2_card = cards.random_card()
            game.player_2_value = cards.values.get(cards.random_value)
            print(f'Player 2 drew {player_2_card}')
            # time.sleep(1)

            if game.player_1_value > game.player_2_value:
                game.player_1_score += 1
            elif game.player_2_value > game.player_1_value:
                game.player_2_score += 1
            else:
                game.player_1_score += 0.5
                game.player_2_score += 0.5
        
        game.check_winner()


cards = Cards()
game = Games()

game.war()
