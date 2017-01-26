import pygame
import random

class Cards:
    # Create and shuffle decks
    def __init__(self):
        self.normaldeck1 = ['fmj', 'fmj', 'rif', 'rif', 'arif', 'arif', 'navm', 'navm', 'navm', 'navm', 'navm', 'navm',
                           'emp', 'emp', 'emp', 'emp', 'refh', 'refh', 'son', 'son', 'son', 'son', 'son', 'smok', 'smok',
                           'sab', 'sab', 'back', 'back', 'fue2', 'fue2', 'fue2', 'fue2', 'fuel', 'fuel', 'fuel', 'fuel',
                           'fuel', 'fuel', 'rally', 'adr', 'adr', 'adr', 'adr']
        self.normaldeck2 = []
        self.specialdeck = ['rep', 'rep', 'flak', 'flak', 'hack', 'far', 'alu', 'pir']
        random.shuffle(self.normaldeck1)
        random.shuffle(self.specialdeck)

    # Shuffle decks
    def shuffle_normaldeck1(self):
        random.shuffle(self.normaldeck1)

    def shuffle_normaldeck2(self):
        random.shuffle(self.normaldeck2)

    # Take a card from normal deck 1
    def pick_normal1(self):
        x = random.randrange(len(self.normaldeck1))
        return self.normaldeck1.pop(x)

    # Take a card from normal deck 2
    def pick_normal2(self):
        x = random.randrange(len(self.normaldeck2))
        return self.normaldeck2.pop(x)

    # Take a card from special deck
    def pick_special(self):
        x = random.randrange(len(self.specialdeck))
        return self.specialdeck.pop(x)
