import pygame

class Tile:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.ship = None
        self.width = width
        self.height = height
        self.selected = False
        self.with_move_range = False
        self.with_fire_range = False
        self.rect = pygame.rect.Rect(x * width, y * height, width, height)

    # Assigns a ship to this tile.
    def set_ship(self, ship):
        self.ship = ship

    # Updates the state of this tile.
    def update(self):
        pass

    # Resets drawing flags for this tile
    def reset(self):
        self.with_fire_range = False
        self.with_move_range = False
        self.selected = False

    # Draws this tile.
    def draw(self, surface):
        if self.selected:
            pygame.draw.rect(surface, (255, 0, 0), self.rect, 2)
        if self.with_move_range:
            pygame.draw.rect(surface, (0, 255, 0), self.rect, 2)
        if self.with_fire_range:
            pygame.draw.rect(surface, (0, 0, 255), self.rect, 1)
        else:
            pygame.draw.rect(surface, (0, 0, 0), self.rect, 1)