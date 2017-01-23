import pygame

import screens.pregame.pregame_instructions
import screens.sound as sound

import widget.button

class RulesScreen:
    def __init__(self, game, prev=None):
        self.game = game
        self.prev = prev
        self.image = pygame.image.load('resources/screens/' + game.language + '/pregame/pregame_rules.jpg')
        self.return_to_prev = widget.button.Button((17, 595), (91, 75), self.xd)

    # Updates this 'pregame rules' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.return_to_prev.on_event(event)

    # TODO
    def xd(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.set_screen(self.prev)

    # Draws the components of this 'pregame rules' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))