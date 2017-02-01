import pygame
# import db.db_service
import screens.game.cards

class Card:
    def __init__(self, id, type, lang):
        self.id = id
        self.type = type
        self.language = lang
        self.image = pygame.image.load('resources/cards/' + type + '/' + self.language + '/' + id + '.jpg')

        # Name = self.id
        # Type = self.type
        # Lang = self.language
        #
        # db.db_service.execute("INSERT INTO Cards (CName, CType, CLang) VALUES (" + str(Name) + "," + str(Type) + "," + str(Lang) + ");")
        #
        # lang = English / Dutch

    # Draws this card on the given surface
    def draw(self, surface, pos):
        surface.blit(self.image, screens.game.cards.CardPositions[pos])