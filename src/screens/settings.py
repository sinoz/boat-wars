import pygame

import widget.button

import screens.main_menu
import screens.canvas
import screens.sound as sound

class SettingsScreen:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont("monospace", 45)
        self.image = pygame.image.load('resources/screens/' + game.language + '/options_menu.jpg')

        # Return button
        self.return_button = widget.button.Button((17, 595), (91, 75), self.return_to_main)

        # Language buttons
        self.change_lang_dutch = widget.button.Button((801, 312), (95, 85), self.change_lang_to_dutch)
        self.change_lang_english = widget.button.Button((629, 313), (96, 93), self.change_lang_to_english)

        # Volume buttons
        self.inc_volume = widget.button.Button((809, 163), (56, 75), self.increase_volume)
        self.dec_volume = widget.button.Button((618, 185), (73, 81), self.decrease_volume)

    # Updates this 'settings' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.return_button.on_event(event)
        self.change_lang_dutch.on_event(event)
        self.change_lang_english.on_event(event)

        self.inc_volume.on_event(event)
        self.dec_volume.on_event(event)

    # Reacts to the user pressing on the 'increase volume' button
    def increase_volume(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.set_volume(self.game.volume + 25)

    # Reacts to the user pressing on the 'decrease volume' button
    def decrease_volume(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.set_volume(self.game.volume - 25)

    # Reacts to the user pressing on the english language toggling button
    def change_lang_to_english(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.change_language(screens.canvas.English)
        self.game.set_screen(SettingsScreen(self.game))

    # Reacts to the user pressing on the dutch language toggling button
    def change_lang_to_dutch(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.change_language(screens.canvas.Dutch)
        self.game.set_screen(SettingsScreen(self.game))

    # Reacts to the user pressing the 'return' button
    def return_to_main(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.set_screen(screens.main_menu.MainScreen(self.game))

    # Draws the components of this 'settings' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))

        label = self.font.render(str(self.game.volume), 1, (0, 0, 0))
        self.game.surface.blit(label, (715, 201))
