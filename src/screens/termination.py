import pygame
import widget.button
import screens.sound as sound

class ExitScreen:
    def __init__(self, game, prev=None):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/termination.jpg')
        self.close_app = widget.button.Button((340, 350), (84, 80), self.close_app)
        self.return_button = widget.button.Button((599, 351), (87, 76), self.return_to_prev)
        self.prev = prev

    # Updates this 'termination' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.close_app.on_event(event)
        self.return_button.on_event(event)

    # Reacts to the user confirming to close the application
    def close_app(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.quitGame()

    # Reacts to the user confirming to return to the previous screen
    def return_to_prev(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.set_screen(self.prev)

    # Draws the components of this 'termination' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))
