import pygame

from intro import IntroductionScreen
from rules import RulesScreen

class InstructionsScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/instr.jpg')

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
                self.game.set_screen(IntroductionScreen(self.game))
            elif x >= 623 and y >= 218 and x <= 916 and y <= 298:
                self.game.set_screen(RulesScreen(self.game))
            elif x >= 395 and y >= 530 and x <= 652 and y <= 614:
                from main_menu import MainScreen
                self.game.set_screen(MainScreen(self.game))

    # Draws the components of this 'settings' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))