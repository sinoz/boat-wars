import pygame

from highscores import HighscoresScreen
from settings import SettingsScreen
from credits import CreditsScreen

class MainScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/main_menu.jpg')

        pygame.mixer.music.load('resources/mp3/intro.mp3')
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(self.game.volume)

    # Draws the components of this main menu screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))

    # Handles an event.
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_cursor = pygame.mouse.get_cursor()
            mouse_pos = pygame.mouse.get_pos()

            # Plays click sound
            def click_sound():
                Click = pygame.mixer.Sound('resources/mp3/Click.ogg')
                pygame.mixer.Sound.play(Click)
                Click.set_volume(0.8)

            x = mouse_pos[0]
            y = mouse_pos[1]

            if x >= 350 and y >= 140 and x <= 670 and y <= 214:
                from exp import ExperienceInstructionsScreen
                self.game.set_screen(ExperienceInstructionsScreen(self.game))
                click_sound()
            elif x >= 354 and y >= 250 and x <= 668 and y <= 320:
                from instructions import InstructionsScreen
                self.game.set_screen(InstructionsScreen(self.game))
                click_sound()
            elif x >= 359 and y >= 355 and x <= 670 and y <= 428:
                self.game.set_screen(SettingsScreen(self.game))
                click_sound()
            elif x >= 356 and y >= 458 and x <= 667 and y <= 538:
                self.game.set_screen(HighscoresScreen(self.game))
                click_sound()
            elif x >= 914 and y >= 603 and x <= 1001 and y <= 679:
                self.game.set_screen(CreditsScreen(self.game))
                click_sound()

    # Updates this main menu screen.
    def update(self):
        pass