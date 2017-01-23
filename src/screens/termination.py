import pygame
import screens.sound as sound

class ExitScreen:
    def __init__(self, game, prev=None):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/termination.jpg')
        self.prev = prev

    # Updates this 'termination' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_cursor = pygame.mouse.get_cursor()
            mouse_pos = pygame.mouse.get_pos()

            x = mouse_pos[0]
            y = mouse_pos[1]

            if x >= 340 and x <= 424 and y >= 350 and y <= 430:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.quitGame()
            elif x >= 599 and x <= 686 and y >= 351 and y <= 427:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(self.prev)

            print(x, y)

    # Draws the components of this 'termination' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))
