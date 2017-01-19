import pygame

from highscores import HighscoresScreen
from settings import SettingsScreen
from getting_started import GettingStartedScreen

class MainScreen:
    def __init__(self, game, app, surface):
        self.game = game
        self.surface = surface
        self.image = pygame.image.load('resources/screens/main_menu.jpg')
        self.app = app

    # Draws the components of this main menu screen.
    def draw(self):
        self.surface.blit(self.image, (0, 0))

    # Handles an event.
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_cursor = pygame.mouse.get_cursor()
            mouse_pos = pygame.mouse.get_pos()

            x = mouse_pos[0]
            y = mouse_pos[1]

            if x >= 350 and y >= 140 and x <= 670 and y <= 214:
                from game import GameScreen
                self.game.set_screen(GameScreen(self.surface))
            elif x >= 354 and y >= 250 and x <= 668 and y <= 320:
                self.game.set_screen(GettingStartedScreen(self.surface))
            elif x >= 359 and y >= 355 and x <= 670 and y <= 428:
                self.game.set_screen(SettingsScreen(self.surface))
            elif x >= 356 and y >= 458 and x <= 667 and y <= 538:
                self.game.set_screen(HighscoresScreen(self.surface))

    # Updates this main menu screen.
    def update(self):
        pass