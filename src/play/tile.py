import pygame

class Tile:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.ship = None
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.rect.Rect(x * width, y * height, width, height)

    # Assigns a ship to this tile.
    def set_ship(self, ship):
        self.ship = ship

    # Updates the state of this tile.
    def update(self):
        pass

    # Draws this tile.
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 1)