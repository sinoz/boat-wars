import pygame

import widget.button

class CardScreen:
    def __init__(self, canvas, prev=None):
        self.canvas = canvas
        self.prev = prev
        self.image = pygame.image.load('resources/screens/' + canvas.language + '/game/cards.png')

        self.return_button = widget.button.Button((41, 611), (90, 58), self.return_to_game)

    # Updates this 'game' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.return_button.on_event(event)

    # Reacts to the user pressing on the return button
    def return_to_game(self, x, y, cursor):
        self.canvas.set_screen(self.prev)

    # Draws the components of this 'game' screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))