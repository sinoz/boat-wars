import pygame

from main_menu import MainScreen

class Game:
    def __init__(self, app, surface, running=True):
        self.app = app
        self.surface = surface
        self.running = running
        self.screen = None

        # NOTE: if you're working on a separate screen (such as hiscores, you can simply
        # change the MainScreen() to your own implementation. Ensure however that your
        # implementation contains the `update()` and `draw()` methods
        self.set_screen(MainScreen(self, app, surface))

    # Polls events from the event queue to deal with. Should only be used for global events
    # that apply for all types of screens.
    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.quitGame()
            else:
                self.screen.on_event(event)

    # Updates the current screen
    def set_screen(self, screen):
        self.screen = screen

    # The game loop that continuously runs until the `self.running` flag equals false.
    def game_loop(self):
        while self.running:
            self.update()
            self.draw()

    # Forces the game to stop running.
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

class GameScreen:
    def __init__(self, surface):
        self.surface = surface

    # Updates this 'getting started' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        pass

    # Draws the components of this 'getting started' screen.
    def draw(self):
        pass