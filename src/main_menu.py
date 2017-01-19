import pygame

from highscores import HighscoresScreen
from settings import SettingsScreen
from credits import CreditsScreen
from exp import ExperienceScreen
from instructions import InstructionsScreen

class MainScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/main_menu.jpg')

    # Draws the components of this main menu screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))

    # Handles an event.
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_cursor = pygame.mouse.get_cursor()
            mouse_pos = pygame.mouse.get_pos()

            x = mouse_pos[0]
            y = mouse_pos[1]

            if x >= 350 and y >= 140 and x <= 670 and y <= 214:
                self.game.set_screen(ExperienceScreen(self.game))
            elif x >= 354 and y >= 250 and x <= 668 and y <= 320:
                self.game.set_screen(InstructionsScreen(self.game))
            elif x >= 359 and y >= 355 and x <= 670 and y <= 428:
                self.game.set_screen(SettingsScreen(self.game))
            elif x >= 356 and y >= 458 and x <= 667 and y <= 538:
                self.game.set_screen(HighscoresScreen(self.game))
            elif x >= 914 and y >= 603 and x <= 1001 and y <= 679:
                self.game.set_screen(CreditsScreen(self.game))

    # Updates this main menu screen.
    def update(self):
        pass