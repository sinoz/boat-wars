import pygame

import screens
import screens.boats
import screens.introduction
import screens.rules
import screens.main_menu
import screens.sound as sound

import widget.button

class InstructionsScreen:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = pygame.image.load('resources/screens/' + canvas.language + '/instructions.jpg')

        self.to_main = widget.button.Button((20, 598), (85, 66), self.return_to_main)
        self.to_intro = widget.button.Button((109, 226), (290, 82), self.open_intro_screen)
        self.to_rules = widget.button.Button((626, 221), (296, 84), self.open_rules_screen)
        self.to_boats = widget.button.Button((409, 444), (199, 81), self.open_boats_screen)

    # Updates this 'settings' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        self.to_main.on_event(event)
        self.to_intro.on_event(event)
        self.to_rules.on_event(event)
        self.to_boats.on_event(event)

    # Opens up the introduction screen.
    def open_intro_screen(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.canvas.set_screen(screens.introduction.IntroductionScreen(self.canvas, self))

    # Opens up the rules screen.
    def open_rules_screen(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.canvas.set_screen(screens.rules.RulesScreen(self.canvas))

    # Opens up the boats screen.
    def open_boats_screen(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.canvas.set_screen(screens.boats.BoatsScreen(self.canvas, self))

    # Returns to the main menu screen.
    def return_to_main(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.canvas.set_screen(screens.main_menu.MainScreen(self.canvas))

    # Draws the components of this 'instructions' screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))