import pygame

class Game:
    def __init__(self, surface, screen, running=True):
        self.surface = surface
        self.running = running
        self.screen = screen

    def poll_events(self):
        # Wait for user events and react
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def game_loop(self):
        while self.running:
            self.poll_events()
            self.update()
            self.draw()

    def update(self):
        self.screen.update()

    def draw(self):
        self.surface.fill((0, 255, 0))  # Green background
        pygame.display.flip()  # Flips the graphics buffers to draw what's on the `screen`