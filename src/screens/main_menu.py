import pygame

import screens.credits as credits
import screens.highscores as highscores
import screens.settings as settings
import screens.experience as exp
import screens.instructions as instructions
import screens.sound as sound

class MainScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/main_menu.jpg')
        sound.Plopperdeplop.music(self, 'intro')

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
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(exp.ExperienceScreen(self.game))
            elif x >= 354 and y >= 250 and x <= 668 and y <= 320:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(instructions.InstructionsScreen(self.game))
            elif x >= 359 and y >= 355 and x <= 670 and y <= 428:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(settings.SettingsScreen(self.game))
            elif x >= 356 and y >= 458 and x <= 667 and y <= 538:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(highscores.HighscoresScreen(self.game))
            elif x >= 914 and y >= 603 and x <= 1001 and y <= 679:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(credits.CreditsScreen(self.game))

    # Updates this main menu screen.
    def update(self):
        pass
