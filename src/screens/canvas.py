import pygame

import play.grid
import screens.main_menu
import screens.game.game
from screens.termination import ExitScreen

Dutch = "nl"
English = "eng"

class Canvas:
    def __init__(self, app, surface, running=True):
        self.app = app
        self.surface = surface
        self.running = running
        self.screen = None
        self.language = English
        self.volume = 100
        self.activeTextField = None
        self.grid = play.grid.Grid(surface, 20, 20)

        # NOTE: if you're working on a separate screen (such as hiscores, you can simply
        # change the MainScreen() to your own implementation. Ensure however that your
        # implementation contains the `update()` and `draw()` methods
        self.set_screen(screens.main_menu.MainScreen(self))

    # Polls events from the event queue to deal with. Should only be used for global events
    # that apply for all types of screens.
    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.set_screen(ExitScreen(self, self.screen))
            else:
                self.screen.on_event(event)

    # Updates the current volume
    def set_volume(self, volume):
        if volume < 0 or volume > 100:
            return
        self.volume = volume
        pygame.mixer.music.set_volume(volume/100)

    # Updates the language
    def change_language(self, language):
        self.language = language

    # Updates the current screen
    def set_screen(self, screen):
        self.screen = screen

    # Applies a keyboard focus on the specified widget
    def apply_keyboard_focus(self, widget):
        self.activeTextField = widget

    # The play loop that continuously runs until the `self.running` flag equals false.
    def game_loop(self):
        while self.running:
            self.update()
            self.draw()

    # Forces the play to stop running.
    def quitGame(self):
        self.running = False

    # Calls for an update on the current screen.
    def update(self):
        self.poll_events()
        self.screen.update()

    # Draws all of the recent updates
    def draw(self):
        self.surface.fill((0, 0, 0))  # Black background
        self.screen.draw()

        pygame.display.flip()  # Flips the graphics buffers to draw what's on the `screen`