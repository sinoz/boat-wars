import pygame

import screens.pregame.pregame_instructions
import screens.game
import screens.sound as sound

class ExperienceScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/experience.jpg')

    # Updates this 'experience' screen.
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
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(screens.game.GameScreen(self.game))
            elif x >= 619 and y >= 379 and x <= 708 and y <= 454:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(screens.pregame.pregame_instructions.PreGameInstructionsScreen(self.game))

    # Draws the components of this 'experience' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))