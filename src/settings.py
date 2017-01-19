import pygame

class SettingsScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/options_menu.jpg')

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
            elif x >= 616 and x <= 667 and y >= 164 and y <= 237: #TODO
                pass # TODO lower volume by 25
            elif x >= 809 and x <= 865 and y >= 163 and y <= 238: #TODO
                pass # TODO up volume by 25

    # Draws the components of this 'settings' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))