import pygame

from exp_instr import ExperienceInstructionsScreen

class ExperienceScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/exp.jpg')

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

            if x >= 311 and y >= 378 and x <= 395 and y <= 456:
                from game import GameScreen
                self.game.set_screen(GameScreen(self.game))
            elif x >= 619 and y >= 379 and x <= 708 and y <= 454:
                self.game.set_screen(ExperienceInstructionsScreen(self.game))

    # Draws the components of this 'settings' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))