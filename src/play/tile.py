import pygame

class Tile:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.rect.Rect(x * width, y * height, width, height)

    # Updates the state of this tile
    def update(self):
        pass

    # Draws the components of this tile
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, self.width)