import pygame

class ExperienceInstructionsScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/exp_instr.jpg')

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

            if x >= 175 and y >= 526 and x <= 452 and y <= 611:
                from main_menu import MainScreen
                self.game.set_screen(MainScreen(self.game))
            elif x >= 106 and y >= 225 and x <= 402 and y <= 306:
                from intro_exp import IntroductionScreen
                self.game.set_screen(IntroductionScreen(self.game))
            elif x >= 623 and y >= 219 and x <= 925 and y <= 303:
                from rules_exp import RulesScreen
                self.game.set_screen(RulesScreen(self.game))
            elif x >= 593 and y >= 523 and x <= 887 and y <= 604:
                from game import GameScreen
                self.game.set_screen(GameScreen(self.game))

    # Draws the components of this 'settings' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))