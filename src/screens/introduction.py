import pygame

import widget.button

class IntroductionScreen:
    def __init__(self, canvas, prev=None):
        self.canvas = canvas
        self.prev = prev
        self.image = pygame.image.load('resources/screens/' + canvas.language + '/introduction.jpg')
        self.return_button = widget.button.Button((17, 595), (91, 75), self.return_to_prev)

    # Updates this 'introduction' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.return_button.on_event(event)

    # Updates the screen back to the previous one
    def return_to_prev(self, x, y, cursor):
        self.canvas.set_screen(self.prev)

    # Draws the components of this 'introduction' screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))