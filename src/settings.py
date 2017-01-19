import pygame
import game

class SettingsScreen:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont("monospace", 45)
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

            if x >= 406 and x <= 654 and y >= 555 and y <= 649:
                from main_menu import MainScreen
                self.game.set_screen(MainScreen(self.game))
            elif x >= 618 and x <= 691 and y >= 185 and y <= 266: #TODO
                self.game.set_volume(self.game.volume - 25)
            elif x >= 809 and x <= 865 and y >= 163 and y <= 238: #TODO
                self.game.set_volume(self.game.volume + 25)
            elif x >= 629 and x <= 725 and y >= 313 and y <= 406:
                self.game.change_language(game.English)
                self.game.set_screen(SettingsScreen(self.game))
            elif x >= 801 and x <= 896 and y >= 312 and y <= 397:
                self.game.change_language(game.Dutch)
                self.game.set_screen(SettingsScreen(self.game))

    # Draws the components of this 'settings' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))

        label = self.font.render(str(self.game.volume), 1, (0, 0, 0))
        self.game.surface.blit(label, (715, 201))