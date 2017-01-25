import pygame

DefenseMode = 0
AttackMode = 1

Scout = 0 # size 2
Avenger = 1 # size 3?
QueenMary = 2 # size 3

class Ship:
    def __init__(self, position, type=Scout, mode=AttackMode):
        self.mode = mode
        self.type = type
        self.position = position
        self.image = pygame.image.load('resources/boats/' + str(type) + '.png')

    # Switches the state of this ship to Attack mode.
    def switch_attack_mode(self):
        self.mode = AttackMode
        # TODO

    # Switches the state of this ship to Defense mode.
    def switch_defense_mode(self):
        self.mode = DefenseMode
        # TODO

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
        surface.blit(self.image, self.position.rect)