import pygame

class Game:
    def __init__(self, surface, screen, running=True):
        self.surface = surface
        self.running = running
        self.screen = screen

    # Polls events from the event queue to deal with
    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quitGame()

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
        self.surface.fill((0, 255, 0))  # Black background
        self.screen.draw()

        pygame.display.flip()  # Flips the graphics buffers to draw what's on the `screen`