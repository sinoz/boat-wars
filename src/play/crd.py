import pygame

import screens.game.cards

class Card:
    def __init__(self, id, type, lang):
        self.id = id
        self.type = type
        self.language = lang
        self.image = pygame.image.load('resources/cards/' + type + '/' + self.language + '/' + id + '.jpg')

        # x = 0 + self.tile.x
        # y = 0 + self.tile.y
        # health = 0 + self.health
        # typ3 = self.type
        # mode = self.mode            #0 = Defense, 1 = Attack, for further coding.
        # firerange = 0 + self.firerange
        # firepower =0 + self.firepower
        #                             # For the coming: False = Negative, True = Applied
        # applied_smokescreen = self.applied_smokescreen
        # mine_armor = self.mine_armor
        # sabotage = self.sabotage
        # remaining_tiles = self.remaining_tiles
        #
        # db.db_service.execute("INSERT INTO into Boats (XPos, YPos, HP, BType, State, BRange, Attack, ShotDef, MineDef, ReflDef, BoatMovementLeft) VALUES (" + str(x) + str(y) + str(health) + str(typ3) + str(mode) + str(firerange) + str(firepower) + str(applied_smokescreen) + str(mine_armor) + str(sabotage) + str(remaining_tiles));
        #
        # lang = English / Dutch
    # Draws this card on the given surface
    def draw(self, surface, pos):
        surface.blit(self.image, screens.game.cards.CardPositions[pos])