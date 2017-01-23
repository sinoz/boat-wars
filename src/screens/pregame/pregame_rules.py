import pygame

import screens.pregame.pregame_instructions
import screens.sound as sound

import widget.button

class RulesScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/pregame/pregame_rules.jpg')
        self.to_rules = widget.button.Button((385, 587), (296, 80), lambda x, y, cursor: self.xd)
        sound.Plopperdeplop.music(self, 'intro')

    # Updates this 'pregame rules' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.to_rules.on_event(event)

    # TODO
    def xd(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.set_screen(screens.pregame.pregame_instructions.PreGameInstructionsScreen(self.game))

    # Draws the components of this 'pregame rules' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))