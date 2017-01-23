import pygame

import screens.instructions

class RulesScreen:
    def __init__(self, game, prev=None):
        self.game = game
        self.prev = prev
        self.image = pygame.image.load('resources/screens/' + game.language + '/rules.jpg')

    # Updates this 'rules' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_cursor = pygame.mouse.get_cursor()
            mouse_pos = pygame.mouse.get_pos()

            x = mouse_pos[0]
            y = mouse_pos[1]
            if x >= 384 and y >= 587 and x <= 683 and y <= 667:
                self.game.set_screen(self.prev)

    # Draws the components of this 'rules' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))