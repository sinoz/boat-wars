import pygame.mixer
import pygame.sysfont

import screens.main_menu
import screens.sound as sound

import widget.button

pygame.init()

class CreditsScreen:
    def __init__(self, game):
        self.image = pygame.image.load('resources/screens/' + game.language + '/credits.jpg')
        self.game = game
        self.return_button = widget.button.Button((20, 604), (88, 72), self.return_to_main)

    # Updates this 'credits' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.return_button.on_event(event)

    # Reacts to the user pressing on the return button
    def return_to_main(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.set_screen(screens.main_menu.MainScreen(self.game))

    # Draws the components of this 'credits' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))
