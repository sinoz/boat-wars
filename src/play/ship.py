import pygame
import db.db_service

DefenseMode = 0
AttackMode = 1

# Id, Size, Moverange, Healthpoints, Firerange, Firepower, Cannon sound
# TODO use a dictionary instead?
Scout = (0, 2, 4, 4, 3, 2, 'cannon_small')
Avenger = (1, 3, 3, 5, 4, 3, 'cannon_big')
QueenMary = (2, 4, 2, 6, 4, 4, 'cannon_big')

class Ship:
    def __init__(self, tile, owner, type=Scout, mode=AttackMode):
        self.type = type

        self.id = type[0]

        self.x = tile.x
        self.y = tile.y

        self.tile = tile

        self.font = pygame.font.SysFont("monospace", 30, 1)
        self.image = pygame.image.load('resources/ships/' + str(type[0]) + '.png')

        self.rect = pygame.rect.Rect(self.x * self.tile.width, self.y * self.tile.height, self.tile.width, self.tile.height)

        self.owner = owner
        self.tile.set_ship(self)

        self.fire_count = 0

        # Gameplay attributes of the ship
        self.mode = mode
        self.size = type[1]
        self.moverange = type[2]
        self.health = type[3]
        self.firerange = type[4]
        self.firepower = type[5]
        self.cannon_sound = type[6]

        # The amount of tiles the ship has left to move over
        self.remaining_tiles = self.moverange

        # The amount of remaining times a ship can attack other ship
        self.firelimit = 1

        # Card effects
        self.fmj_upgrade = True
        self.rifling = False
        self.better_rifling = False
        self.reinforced_hull = False
        self.applied_smokescreen = False
        self.sabotage = False
        self.extra_fuel = False
        self.extra_fuel_two = False
        self. rally = False
        self.adrenaline_rush = False
        self.repair = False
        self.mine_armor = False
        self.far_sight = False
        self.alumininum_hull = False

        #Save the Boat info in the databse
        x = 0 + self.tile.x
        y = 0 + self.tile.y
        health = 0 + self.health
        BID = self.id
        mode = self.mode  # 0 = Defense, 1 = Attack, for further coding.
        firerange = 0 + self.firerange
        firepower = 0 + self.firepower
        # For the coming: False = Negative, True = Applied
        applied_smokescreen = self.applied_smokescreen
        mine_armor = self.mine_armor
        sabotage = self.sabotage
        remaining_tiles = self.remaining_tiles

        db.db_service.execute("INSERT INTO Boats (XPos, YPos, HP, BID, State, BRange, Attack, ShotDef, MineDef, ReflDef, BoatMovementLeft) VALUES (" + str(x) + "," + str(y) + "," + str(health) + "," + str(BID) + "," + str(mode) + "," + str(firerange) + "," + str(firepower) + "," + str(applied_smokescreen) + "," + str(mine_armor) + "," + str(sabotage) + "," + str(remaining_tiles) + ");")

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
        return self.remaining_tiles == 0

    # Resets all of its action counters.
    def reset_counts(self):
        self.remaining_tiles = self.moverange
        self.fire_count = 0

    # Apply card effects
    def apply_card_effect(self, card):
        if card.id == 'refh':
            self.health += 1

        print(card.id)

    # Resets all of the card flags of attack related effects that only last for a single attack.
    def reset_attack_effects(self):
        self.fmj_upgrade = False
        self.rifling = False
        self.better_rifling = False

        # Reset all of the stats back to its original state
        self.reset_firepower()
        self.reset_firerange()
        self.reset_moverange()

    # Resets the moverange back to its original state
    def reset_moverange(self):
        self.moverange = self.type[2]

    # Resets the firerange back to its original state
    def reset_firerange(self):
        self.firerange = self.type[4]

    # Resets the firepower back to its original state
    def reset_firepower(self):
        self.firepower = self.type[5]

    # Updates the state of this ship per frame.
    def update(self):
        pass

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