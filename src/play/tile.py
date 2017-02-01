import pygame

Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
Black = (0, 0, 0)

class Tile:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.ship = None
        self.mine = None
        self.width = width
        self.height = height
        self.selected = False
        self.with_move_range = False
        self.with_fire_range = False
        self.marked = False
        self.rect = pygame.rect.Rect(x * width, y * height, width, height)

    # Assigns a ship to this tile.
    def set_ship(self, ship):
        self.ship = ship

    # Assigns a mine to this tile
    def set_mine(self, mine):
        self.mine = mine

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
        if not self.ship is None and not self.ship.owner.session.selected_ship_card is None:
            # We mark the ships of the player whose turn it is as green and the opponent as red
            if self.ship.owner == self.ship.owner.session.current_turn:
                self.draw_rect(surface, Green)
            else:
                self.draw_rect(surface, Red)
        elif not self.mine is None and not self.mine.session.selected_mine_card is None:
            self.draw_rect(surface, Green)
        else:
            if self.marked:
                self.draw_rect(surface, Green)
            elif self.with_move_range:
                self.draw_rect(surface, Yellow)
            elif self.with_fire_range:
                self.draw_rect(surface, Red)
            else:
                self.draw_rect(surface, Black)

    # Draws a coloured rectangle on the specified surface
    def draw_rect(self, surface, color):
        pygame.draw.rect(surface, color, self.rect, 1)