import pygame.mixer
import pygame.sysfont

import screens.main_menu
import screens.sound as sound

import widget.button

pygame.init()

class BoatsScreen:
    def __init__(self, canvas, prev):
        self.image = pygame.image.load('resources/screens/' + canvas.language + '/game/boats.jpg')
        self.canvas = canvas
        self.prev = prev
        self.return_button = widget.button.Button((20, 604), (88, 72), self.return_to_main)

    # Updates this 'boats' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.return_button.on_event(event)

    # Reacts to the user pressing on the return button
    def return_to_main(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.canvas.set_screen(self.prev)

    # Draws the components of this 'boats' screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))
