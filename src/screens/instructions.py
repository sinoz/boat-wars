import pygame

import screens

import screens.introduction
import screens.rules
import screens.sound as sound

class InstructionsScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/instructions.jpg')

    # Updates this 'settings' screen.
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

            if x >= 106 and y >= 223 and x <= 400 and x <= 304:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(screens.introduction.IntroductionScreen(self.game))
            elif x >= 623 and y >= 218 and x <= 916 and y <= 298:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(screens.rules.RulesScreen(self.game))
            elif x >= 395 and y >= 530 and x <= 652 and y <= 614:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(screens.main_menu.MainScreen(self.game))

    # Draws the components of this 'instructions' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))