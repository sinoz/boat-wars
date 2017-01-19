import pygame

class SettingsScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/options_menu.jpg')

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

            if x >= 379 and x <= 657 and y >= 510 and y <= 591:
                from main_menu import MainScreen
                self.game.set_screen(MainScreen(self.game))

    # Draws the components of this 'settings' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))