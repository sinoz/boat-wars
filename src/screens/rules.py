import pygame

import screens.instructions
import screens.sound as sound

class RulesScreen:
    def __init__(self, game):
        self.game = game
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

            print(x, y)

            if x >= 384 and y >= 587 and x <= 683 and y <= 667:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(screens.instructions.InstructionsScreen(self.game))

    # Draws the components of this 'rules' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))