import pygame

import screens.instructions
import screens.sound as sound

import widget.button
import screens.instructions

class RulesScreen:
    def __init__(self, game, prev=None):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/rules.jpg')
        self.return_button = widget.button.Button((17, 595), (91, 75), self.return_to_prev)

    # Updates this 'rules' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.return_button.on_event(event)

    # TODO
    def return_to_prev(self, x, y, cursor):
        self.game.set_screen(screens.instructions.InstructionsScreen(self.game))
        sound.Plopperdeplop.tune(self, 'click')

    # Draws the components of this 'rules' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))