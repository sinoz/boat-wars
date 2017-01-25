import pygame

import screens.credits as credits
import screens.highscores as highscores
import screens.settings as settings
import screens.experience as exp
import screens.instructions as instructions
import screens.sound as sound

class MainScreen:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = pygame.image.load('resources/screens/' + canvas.language + '/main_menu.jpg')
        if sound.current_song != 'intro':
            sound.Plopperdeplop.music(self, 'intro')

    # Draws the components of this main menu screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))

    # Handles an event.
    def on_event(self, event): # TODO use widget.button instead of hardcoding
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_cursor = pygame.mouse.get_cursor()
            mouse_pos = pygame.mouse.get_pos()

            x = mouse_pos[0]
            y = mouse_pos[1]

            if x >= 350 and y >= 140 and x <= 670 and y <= 214:
                sound.Plopperdeplop.tune(self, 'click')
                self.canvas.set_screen(exp.ExperienceScreen(self.canvas))
            elif x >= 354 and y >= 250 and x <= 668 and y <= 320:
                sound.Plopperdeplop.tune(self, 'click')
                self.canvas.set_screen(instructions.InstructionsScreen(self.canvas))
            elif x >= 359 and y >= 355 and x <= 670 and y <= 428:
                sound.Plopperdeplop.tune(self, 'click')
                self.canvas.set_screen(settings.SettingsScreen(self.canvas))
            elif x >= 356 and y >= 458 and x <= 667 and y <= 538:
                sound.Plopperdeplop.tune(self, 'click')
                self.canvas.set_screen(highscores.HighscoresScreen(self.canvas, self))
            elif x >= 914 and y >= 603 and x <= 1001 and y <= 679:
                sound.Plopperdeplop.tune(self, 'click')
                self.canvas.set_screen(credits.CreditsScreen(self.canvas))

    # Updates this main menu screen.
    def update(self):
        pass
