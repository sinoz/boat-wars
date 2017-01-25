import pygame

class Tile:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.ship = None
        self.width = width
        self.height = height
        self.color = color
        self.selected = False
        self.rect = pygame.rect.Rect(x * width, y * height, width, height)

    # Assigns a ship to this tile.
    def set_ship(self, ship):
        self.ship = ship

    # Updates the state of this tile.
    def update(self):
        pass

    # Resets the selection for this tile
    def reset_selection(self):
        self.selected = False

    # Draws this tile.
    def draw(self, surface):
        if not self.selected:
            pygame.draw.rect(surface, self.color, self.rect, 1)
        else:
            pygame.draw.rect(surface, (255, 0, 0), self.rect, 2)