import pygame

import screens.game.game
import screens.main_menu
import widget.button
import widget.text_field

class SessionScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/pregame/names.jpg')

        # The start game button
        self.start_game_button = widget.button.Button((377, 597), (280, 76), self.start_game)

        # The return button
        self.return_button = widget.button.Button((16, 600), (93, 77), self.return_to_main)

        # The username text fields
        self.p1_name = widget.text_field.TextField(game, (105, 380), (250, 250), (0, 0, 0), 30, 12, "Player #1")
        self.p2_name = widget.text_field.TextField(game, (683, 378), (250, 250), (0, 0, 0), 30, 12, "Player #2")

        self.game.apply_keyboard_focus(self.p1_name)

    # Updates this 'session' screen.
    def update(self):
        pass # TODO

    # Handles an event.
    def on_event(self, event):
        self.return_button.on_event(event)
        self.start_game_button.on_event(event)

        # Handle text field events
        self.p1_name.on_event(event)
        self.p2_name.on_event(event)

    # TODO
    def start_game(self, x, y, cursor):
        self.game.set_screen(screens.game.game.GameScreen(self.game))

    # TODO
    def return_to_main(self, x, y, cursor):
        self.game.set_screen(screens.main_menu.MainScreen(self.game))

    # Draws the components of this 'session' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))
        self.p1_name.draw()
        self.p2_name.draw()