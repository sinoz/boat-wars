import pygame

import screens.instructions
import screens.sound as sound

import widget.button
import screens.instructions

class RulesScreen:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = pygame.image.load('resources/screens/' + canvas.language + '/rules.jpg')
        self.return_button = widget.button.Button((17, 595), (91, 75), self.return_to_prev)

    # Updates this 'rules' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.return_button.on_event(event)

    # Returns to the previous screen.
    def return_to_prev(self, x, y, cursor):
        self.canvas.set_screen(screens.instructions.InstructionsScreen(self.canvas))
        sound.Plopperdeplop.tune(self, 'click')

    # Draws the components of this 'rules' screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))