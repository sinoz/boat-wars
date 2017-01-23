import pygame.mixer
import pygame.sysfont

import screens.main_menu
import screens.sound as sound

pygame.init()

class CreditsScreen:
    def __init__(self, game):
        self.image = pygame.image.load('resources/screens/' + game.language + '/credits.jpg')
        self.game = game
        sound.Plopperdeplop.music(self, 'credits')

    # Updates this 'credits' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_cursor = pygame.mouse.get_cursor()
            mouse_pos = pygame.mouse.get_pos()

            x = mouse_pos[0]
            y = mouse_pos[1]

            print(x, y)

            if x >= 421 and y >= 536 and x <= 642 and y <= 628:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(screens.main_menu.MainScreen(self.game))

    # Draws the components of this 'credits' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))
