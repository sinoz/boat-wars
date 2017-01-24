import pygame

import screens
import screens.introduction
import screens.rules
import screens.main_menu
import screens.sound as sound

import widget.button

class InstructionsScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/instructions.jpg')

        self.to_main = widget.button.Button((20, 598), (85, 66), self.return_to_main)
        self.to_intro = widget.button.Button((109, 226), (290, 82), self.open_intro_screen)
        self.to_rules = widget.button.Button((626, 221), (296, 84), self.open_rules_screen)

    # Updates this 'settings' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.to_main.on_event(event)
        self.to_intro.on_event(event)
        self.to_rules.on_event(event)

    # TODO
    def open_intro_screen(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.set_screen(screens.introduction.IntroductionScreen(self.game, self))

    # TODO
    def open_rules_screen(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.set_screen(screens.rules.RulesScreen(self.game))

    # TODO
    def return_to_main(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.set_screen(screens.main_menu.MainScreen(self.game))

    # Draws the components of this 'instructions' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))