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

            if x >= 79 and y >= 290 and x <= 395 and x <= 363:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(screens.introduction.IntroductionScreen(self.game, self))
            elif x >= 622 and y >= 284 and x <= 935 and y <= 362:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(screens.rules.RulesScreen(self.game))
            elif x >= 20 and y >= 598 and x <= 105 and y <= 664:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(screens.main_menu.MainScreen(self.game))

    # Draws the components of this 'instructions' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))