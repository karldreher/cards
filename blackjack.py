import random

values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suits = {'D':"Diamonds",'H':'Hearts','C':'Clubs','S':'Spades'}

deck = []
shuffled_deck = []

class Player:
    def __init__(self):
        self.hand = []


class Card:
	def __init__(self,card_suit,card_value):
		self.suit = card_suit
		self.value = card_value


def shuffle():
    for suit in suits.values():
        for value in values:
            card=Card(suit,value)
            deck.append(card)
    for i in (range(0,(len(deck)))):
        random_card = random.choice(deck)
        deck.remove(random_card)
        shuffled_deck.append(random_card)
        

def deal(player):
    card = shuffled_deck.pop()
    player.hand.append(card)

def score(hand):
    total = 0
    for card in hand:
        if int(card.value):
            points = int(card.value)
        elif card.value in ["J","Q","K"]:
            points = 10
        elif card.value == "A":
            #obviously sorta broken.  OK for now.
            points = 11
        total += points
    return total

if __name__ == "__main__":
    dealer=Player()
