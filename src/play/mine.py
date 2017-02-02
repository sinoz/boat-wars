import pygame
import screens.sound as sound

class Mine:
    def __init__(self, session, tile):
        self.tile = tile
        self.x = tile.x
        self.y = tile.y
        self.session = session
        self.image = pygame.image.load('resources/templates/Sea_mine.png')
        self.rect = pygame.rect.Rect(self.x * self.tile.width, self.y * self.tile.height, self.tile.width, self.tile.height)
        self.tile.set_mine(self)

    # Computes and returns a collection of coordinates that surround this mine.
    def get_surrounding_pos(self, delta):
        positions = []
        for y in range(self.y - delta, self.y + delta):
            for x in range(self.x - delta, self.x + delta):
                positions.append((x, y))
        return positions

    # Clears this mine from the field.
    def clear(self):
        self.tile.set_mine(None)

    # Explodes this mine, damaging all of the specified ships that are in the vicinity.
    def explode(self, ships):
        for ship in ships:
            ship.health -= 2

            if ship.health <= 0:
                sound.Plopperdeplop.tune(self, 'explosion_ship')
                ship.wreck()
                ship.health = 0

        self.clear()

    # Updates the state of this mine per frame
    def update(self):
        pass

    # Draws this mine on the given surface
    def draw(self, surface):

        surface.blit(self.image, self.rect)