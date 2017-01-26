import pygame

DefenseMode = 0
AttackMode = 1

# Id, Size, Moverange, Healthpoints, Firerange, Firepower
# TODO use a dictionary instead?
Scout = (0, 2, 4, 4, 3, 2)
Avenger = (1, 3, 3, 5, 4, 3)
Marejada = (2, 3, 3, 5, 4, 3)
QueenMary = (3, 4, 2, 6, 4, 4)

class Ship:
    def __init__(self, tile, type=Scout, mode=AttackMode):
        self.type = type
        self.x = tile.x
        self.y = tile.y
        self.tile = tile
        self.image = pygame.image.load('resources/ships/' + str(type[0]) + '.png')

        # Gameplay attributes of the ship
        self.mode = mode
        self.size = type[1]
        self.health = type[2]
        self.moverange = type[3]
        self.firerange = type[4]
        self.firepower = type[5]

        self.tile.set_ship(self)

    # Returns a list of tile positions that this ship currently occupies.
    def occupied_tile_pos(self):
        positions = []

        if self.in_attack_mode():
            for y_offset in range(self.size):
                y = self.y + y_offset
                positions.append((self.x, y))
        else:
            for x_offset in range(self.size):
                x = self.x + x_offset
                positions.append((x, self.y))

        return positions

    # Switches the state of this ship to Attack mode.
    def switch_attack_mode(self):
        self.mode = AttackMode
        self.transform(0)

    # Switches the state of this ship to Defense mode.
    def switch_defense_mode(self):
        self.mode = DefenseMode
        self.transform(90)

    # Transforms the image to be set to the specified angle.
    def transform(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)

    # Returns whether this ship is currently in Attack mode or not.
    def in_attack_mode(self):
        return self.mode == AttackMode

    # Returns whether this ship is currently in Defense mode or not.
    def in_defense_mode(self):
        return self.mode == DefenseMode

    # Updates the state of this ship per frame.
    def update(self):
        pass

    # Draws this ship onto the given surface.
    def draw(self, surface):
        surface.blit(self.image, pygame.rect.Rect(self.x * self.tile.width, self.y * self.tile.height, self.tile.width, self.tile.height))