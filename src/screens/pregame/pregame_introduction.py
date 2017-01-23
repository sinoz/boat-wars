import pygame

import screens.pregame.pregame_instructions
import screens.sound as sound

import widget.button

class PreGameIntroductionScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/pregame/pregame_introduction.jpg')
        self.button1 = widget.button.Button((17, 595), (91, 75), self.xd)

    # Updates this 'pregame introduction' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.button1.on_event(event)

    # TODO
    def xd(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.set_screen(screens.pregame.pregame_instructions.PreGameInstructionsScreen(self.game))

    # Draws the components of this 'pregame introduction' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))