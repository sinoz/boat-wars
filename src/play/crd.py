import pygame

class Card:
    def __init__(self, id, type, lang):
        self.id = id
        self.type = type
        self.language = lang
        self.image = pygame.image.load('resources/cards/' + type + '/' + self.language + '/' + id + '.jpg')
        self.positions = [(39,46), (319,47), (604,46), (37,330), (319,329), (602,326)]

    # Draws this card on the given surface
    def draw(self, surface, pos):
        surface.blit(self.image, self.positions[pos])