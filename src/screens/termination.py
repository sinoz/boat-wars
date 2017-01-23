import pygame
import widget.button

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
        self.game.quitGame()
        self.click_sound()

    # Reacts to the user confirming to return to the previous screen
    def return_to_prev(self, x, y, cursor):
        self.game.set_screen(self.prev)
        self.click_sound()

    # Draws the components of this 'termination' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))

    # Plays click sound
    def click_sound(self):
        Click = pygame.mixer.Sound('resources/mp3/Click.ogg')
        pygame.mixer.Sound.play(Click)
        Click.set_volume(0.8)