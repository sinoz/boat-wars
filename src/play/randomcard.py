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

        self.currentdeck = self.normaldeck1

        random.shuffle(self.currentdeck)
        random.shuffle(self.specialdeck)

    # Take a card from currentdeck
    def pick_currentdeck(self):
        return self.normaldeck1.pop()

    # Take a card from special deck
    def pick_special(self):
        return self.specialdeck.pop()
