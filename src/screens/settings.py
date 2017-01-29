import pygame

import widget.button

import screens.main_menu
import screens.canvas
import screens.sound as sound

class SettingsScreen:
    def __init__(self, canvas, prev=None):
        self.canvas = canvas
        self.prev = prev
        self.font = pygame.font.SysFont("monospace", 45)
        self.image = pygame.image.load('resources/screens/' + canvas.language + '/options_menu.jpg')

        # Return button
        self.return_button = widget.button.Button((17, 595), (91, 75), self.return_to_prev)

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
        self.canvas.set_volume(self.canvas.volume + 25)

    # Reacts to the user pressing on the 'decrease volume' button
    def decrease_volume(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.canvas.set_volume(self.canvas.volume - 25)

    # Reacts to the user pressing on the english language toggling button
    def change_lang_to_english(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.canvas.change_language(screens.canvas.English)
        self.canvas.set_screen(SettingsScreen(self.canvas, self.prev))

    # Reacts to the user pressing on the dutch language toggling button
    def change_lang_to_dutch(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.canvas.change_language(screens.canvas.Dutch)
        self.canvas.set_screen(SettingsScreen(self.canvas, self.prev))

    # Reacts to the user pressing the 'return' button
    def return_to_prev(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        print(self.prev)
        self.canvas.set_screen(self.prev)

    # Draws the components of this 'settings' screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))

        label = self.font.render(str(self.canvas.volume), 1, (0, 0, 0))
        surface.blit(label, (715, 201))
