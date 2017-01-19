import pygame.sysfont

class CreditsScreen:
    def __init__(self, game):
        self.image = pygame.image.load('resources/screens/' + game.language + '/credits.jpg')
        self.game = game

    # Updates this 'credits' screen.
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

            if x >= 421 and y >= 536 and x <= 642 and y <= 628:
                from main_menu import MainScreen
                self.game.set_screen(MainScreen(self.game))

    # Draws the components of this 'credits' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))