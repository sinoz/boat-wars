import pygame

class Mine:
    def __init__(self, tile):
        self.x = tile.x
        self.y = tile.y
        self.image = pygame.image.load('resources/templates/sea_mine.jpg')
        self.rect = pygame.rect.Rect(self.x * self.tile.width, self.y * self.height, self.tile.width, self.tile.height)
        self.owner = None
        self.tile.set_mine(self)
        