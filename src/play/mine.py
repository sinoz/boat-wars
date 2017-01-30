import pygame

class Mine:
    def __init__(self, tile):
        self.tile = tile
        self.x = tile.x
        self.y = tile.y
        self.image = pygame.image.load('resources/templates/Sea_mine.png')
        self.rect = pygame.rect.Rect(self.x * self.tile.width, self.y * self.tile.height, self.tile.width, self.tile.height)
        self.owner = None
        self.tile.set_mine(self)

    # Updates the state of this mine per frame
    def update(self):
        pass

    # Draws this mine on the given surface
    def draw(self, surface):
        surface.blit(self.image, self.rect)