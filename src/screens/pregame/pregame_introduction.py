import pygame

import screens.pregame.pregame_instructions

class PreGameIntroductionScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/pregame/pregame_introduction.jpg')

    # Updates this 'pregame introduction' screen.
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

            if x >= 684 and y >= 542 and x <= 1003 and y <= 619:
                self.game.set_screen(screens.pregame.pregame_instructions.PreGameInstructionsScreen(self.game))

    # Draws the components of this 'pregame introduction' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))