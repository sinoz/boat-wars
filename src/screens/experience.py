import pygame

import screens.game.game
import screens.game.set_names
import screens.pregame.pregame_instructions
import screens.game
import screens.sound as sound
import screens.canvas

class ExperienceScreen:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = pygame.image.load('resources/screens/' + canvas.language + '/experience.jpg')

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
                self.canvas.set_screen(screens.game.set_names.SetNamesScreen(self.canvas))
            elif x >= 619 and y >= 379 and x <= 708 and y <= 454:
                sound.Plopperdeplop.tune(self, 'click')
                self.canvas.set_screen(screens.pregame.pregame_instructions.PreGameInstructionsScreen(self.canvas))

    # Draws the components of this 'experience' screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))