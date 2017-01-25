import pygame

DefenseMode = 0
AttackMode = 1

# Id, Size
Scout = (0, 2)
Avenger = (1, 3)
QueenMary = (2, 3)

class Ship:
    def __init__(self, tile, type=Scout, mode=AttackMode):
        self.mode = mode
        self.type = type
        self.x = tile.x
        self.y = tile.y
        self.tile = tile
        self.image = pygame.image.load('resources/ships/' + str(type[0]) + '.png')

        self.tile.set_ship(self)

    # Returns the ship type id.
    def boat_type(self):
        return self.type[0]

    # Returns the size of the ship in tiles
    def boat_size(self):
        return self.type[1]

    # Switches the state of this ship to Attack mode.
    def switch_attack_mode(self):
        self.mode = AttackMode
        self.transform(0)

    # Switches the state of this ship to Defense mode.
    def switch_defense_mode(self):
        self.mode = DefenseMode
        self.transform(90)

        # Avenger ships move one tile to the left to center on top of the exact tile position
        if self.boat_type() == Avenger[0]:
            self.x -= 1

    # Transforms the image to be set to the specified angle.
    def transform(self, angle):
        print("transformed ship")
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