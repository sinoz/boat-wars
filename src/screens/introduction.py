import pygame

import screens.instructions
import screens.sound as sound

class IntroductionScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/introduction.jpg')
        sound.Plopperdeplop.music(self, 'intro')

    # Updates this 'introduction' screen.
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

            print("topkek")
            if x >= 685 and y >= 539 and x <= 1001 and y <= 618:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(screens.instructions.InstructionsScreen(self.game))

    # Draws the components of this 'introduction' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))