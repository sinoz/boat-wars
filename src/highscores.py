import pygame

class HighscoresScreen:
    def __init__(self, game):
        self.image = pygame.image.load('resources/screens/' + game.language + '/highscores.jpg')
        self.game = game

    # Draws the components of this hiscores screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))

    # Handles an event.
    def on_event(self, event):
        pass

    # Updates this hiscores screen.
    def update(self):
        pass