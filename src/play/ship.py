import pygame

DefenseMode = 0
AttackMode = 1

# Id, Size, Moverange, Healthpoints, Firerange, Firepower
# TODO use a dictionary instead?
Scout = (0, 2, 4, 4, 3, 2)
Avenger = (1, 3, 3, 5, 4, 3)
QueenMary = (2, 4, 2, 6, 4, 4)

class Ship:
    def __init__(self, tile, owner, type=Scout, mode=AttackMode):
        self.type = type

        self.x = tile.x
        self.y = tile.y

        self.tile = tile

        self.font = pygame.font.SysFont("monospace", 30, 1)
        self.image = pygame.image.load('resources/ships/' + str(type[0]) + '.png')

        self.rect = pygame.rect.Rect(self.x * self.tile.width, self.y * self.tile.height, self.tile.width, self.tile.height)

        self.owner = owner
        self.tile.set_ship(self)

        self.fire_count = 0
        self.move_count = 0

        # Gameplay attributes of the ship
        self.mode = mode
        self.size = type[1]
        self.moverange = type[2]
        self.health = type[3]
        self.firerange = type[4]
        self.firepower = type[5]
        self.firelimit = 1

        # Card effects
        self.applied_smokescreen = False

    # Updates the grid and pixel coordinates of this ship
    def update_pos(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = x * self.tile.width
        self.rect.y = y * self.tile.height

    # Returns a list of tile positions that this ship would occupy if it were in the specified mode.
    def occupied_tile_pos(self, in_attack_mode):
        positions = []

        if in_attack_mode:
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
        if self.mode != AttackMode:
            self.mode = AttackMode
            self.transform(-90)

    # Switches the state of this ship to Defense mode.
    def switch_defense_mode(self):
        if self.mode != DefenseMode:
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

    # Returns whether this ship has reached its firing limit of 1.
    def reached_fire_limit(self):
        return self.fire_count == self.firelimit

    # Returns whether this ship has reached its moving limit of 1.
    def reached_move_limit(self):
        return self.move_count >= self.moverange

    # Resets all of its action counters.
    def reset_counts(self):
        self.move_count = 0
        self.fire_count = 0

    # Updates the state of this ship per frame.
    def update(self):
        pass # TODO

    # Draws this ship onto the given surface.
    def draw(self, surface):
        surface.blit(self.image, self.rect)

        draw_x = self.x
        draw_y = self.y

        if self.y == 0:
            draw_y += 1

        ship_health = self.font.render(str(self.health), 1, (0, 255, 0))
        ship_health_x = draw_x * self.tile.width
        ship_health_y = draw_y * self.tile.height

        surface.blit(ship_health, (ship_health_x + self.tile.width / 4, ship_health_y - 15))

    # Translates the mode id to a reusable name.
    def mode_id_to_name(self):
        if self.mode == AttackMode:
            return "Attack"
        else:
            return "Defense"