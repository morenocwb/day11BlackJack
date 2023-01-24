import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clean():
    os.system('clear')

def initial_deal_card():
    """Draw Initial Two Cards for the Players"""
    player_cards = []
    # randomize cards drawn
    for _ in range(2):
        drawn_card = deal_card()
        player_cards.append(cards[drawn_card])
        # print(f'that is computer card {player_cards}')

    return player_cards


def deal_card():
    """"Returns a random card from the deck"""
    drawn_card = random.randint(0, 12)
    player_cards = cards[drawn_card]

    return player_cards

def calculate_score(cards):
    return sum(cards)