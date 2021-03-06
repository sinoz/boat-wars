import pygame

import screens.pregame.pregame_instructions
import screens.sound as sound

import widget.button

class PreGameIntroductionScreen:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = pygame.image.load('resources/screens/' + canvas.language + '/pregame/pregame_introduction.jpg')
        self.button1 = widget.button.Button((17, 595), (91, 75), self.to_instructions)

    # Updates this 'pregame introduction' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.button1.on_event(event)

    # Switches to the pre-game instructions screen.
    def to_instructions(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.canvas.set_screen(screens.pregame.pregame_instructions.PreGameInstructionsScreen(self.canvas))

    # Draws the components of this 'pregame introduction' screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))