import pygame.mixer
import pygame.sysfont

import screens.main_menu
import screens.sound as sound

import widget.button

pygame.init()

class CreditsScreen:
    def __init__(self, canvas):
        self.image = pygame.image.load('resources/screens/' + canvas.language + '/credits.jpg')
        self.canvas = canvas
        self.return_button = widget.button.Button((20, 604), (88, 72), self.return_to_main)
        sound.Plopperdeplop.music(self, 'credits')

    # Updates this 'credits' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.return_button.on_event(event)

    # Reacts to the user pressing on the return button
    def return_to_main(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.canvas.set_screen(screens.main_menu.MainScreen(self.canvas))

    # Draws the components of this 'credits' screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))
