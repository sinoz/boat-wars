# import pygame
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
        self.trashdeck = self.normaldeck2

        random.shuffle(self.currentdeck)
        random.shuffle(self.specialdeck)

    # Switch currentdeck
    def check_currentdeck(self):
        if len(self.currentdeck) == 0:
            if self.currentdeck == self.normaldeck1:
                self.currentdeck = self.normaldeck2
                self.trashdeck = self.normaldeck1
                random.shuffle(self.currentdeck)
            else:
                self.currentdeck = self.normaldeck1
                self.trashdeck = self.normaldeck2
                random.shuffle(self.currentdeck)

    # Take a card from currentdeck
    def pick_currentdeck(self):
        card = self.normaldeck1.pop()
        self.check_currentdeck()
        return card

    # Take a card from special deck
    def pick_special(self):
        return self.specialdeck.pop()

    # Add card to trashdeck
    def trash_card(self, card):
        self.trashdeck.append(card)