'''
Card Game Interface
Creator(s): Gage Gunn

Version 1.0
'''

import random

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


class Score:
    def __init__(self, player_1_score, player_2_score):
        self.player_1_score = player_1_score
        self.player_2_score = player_2_score
        self.player_1_value = 0
        self.player_2_value = 0


    def check_winner(self, player_1_score, player_2_score):
        if player_1_score > player_2_score:
            winner = print(f'Player 1 was won with a score of {str(player_1_score)}')
        elif player_2_score > player_1_score:
            winner = print(f'Player 2 has won with a score of {str(player_2_score)}')
        elif player_1_score == player_2_score:
            winner = print('Both players have tied')
        else:
            return False
        return winner

    def reset_score(self):
        self.player_1_score = 0
        self.player_2_score = 0


cards = Cards()
score = Score(0, 0)
