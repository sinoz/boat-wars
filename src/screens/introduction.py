import pygame

import widget.button

class IntroductionScreen:
    def __init__(self, game, prev=None):
        self.game = game
        self.prev = prev
        self.image = pygame.image.load('resources/screens/' + game.language + '/introduction.jpg')
        self.return_button = widget.button.Button((17, 595), (91, 75), lambda x, y, cursor: game.set_screen(prev))

    # Updates this 'introduction' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.return_button.on_event(event)

    # Draws the components of this 'introduction' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))