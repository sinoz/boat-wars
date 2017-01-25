import pygame

import screens.game.game
import screens.main_menu
import play.grid
import play.player
import play.session
import widget.button
import widget.text_field

class SetNamesScreen:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = pygame.image.load('resources/screens/' + canvas.language + '/pregame/names.jpg')

        # The start game button
        self.start_game_button = widget.button.Button((377, 597), (280, 76), self.start_game)

        # The return button
        self.return_button = widget.button.Button((16, 600), (93, 77), self.return_to_main)

        # The username text fields
        self.p1_name = widget.text_field.TextField(canvas, (105, 380), (250, 250), (0, 0, 0), 30, 12, "Player #1")
        self.p2_name = widget.text_field.TextField(canvas, (683, 378), (250, 250), (0, 0, 0), 30, 12, "Player #2")

        self.canvas.apply_keyboard_focus(self.p1_name)

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
        grid = play.grid.Grid(26, 20)
        session = play.session.Session(grid, self.p1_name.text, self.p2_name.text)

        self.canvas.set_screen(screens.game.game.GameScreen(self.canvas, session))

    # TODO
    def return_to_main(self, x, y, cursor):
        self.canvas.set_screen(screens.main_menu.MainScreen(self.canvas))

    # Draws the components of this 'session' screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))

        self.p1_name.draw(surface)
        self.p2_name.draw(surface)