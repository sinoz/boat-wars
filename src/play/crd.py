import pygame

import screens.game.cards

class Card:
    def __init__(self, id, type, lang):
        self.id = id
        self.type = type
        self.language = lang
        self.image = pygame.image.load('resources/cards/' + type + '/' + self.language + '/' + id + '.jpg')

    # Draws this card on the given surface
    def draw(self, surface, pos):
        surface.blit(self.image, screens.game.cards.CardPositions[pos])