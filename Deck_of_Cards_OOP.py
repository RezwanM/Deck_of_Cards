# Code borrowed from: https://www.youtube.com/watch?v=t8YkjDH86Y4

import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    
    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        # Contains a list of Card instances
        self.cards = []
        self.build()

    # build() can also be used separately, e.g. after shuffling deck
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))
    
    def show(self):
        for c in self.cards:
            # This show() is the method of the Card class
            c.show()
    
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def draw(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        # Contains Card instances
        self.hand = []
        self.name = name
    
    def draw(self, deck):
        self.hand.append(deck.draw())
        return self   # To chain the draw() method

    def showHand(self):
        for c in self.hand:
            c.show()
    
    def discard(self):
        return self.hand.pop()



deck = Deck()
deck.shuffle()
bob = Player("Bob")
bob.draw(deck).draw(deck)
bob.showHand()
