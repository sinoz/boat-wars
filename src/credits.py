import pygame.sysfont

class CreditsScreen:
    def __init__(self, app, surface):
        self.font = pygame.font.SysFont("monospace", 20)
        self.app = app
        self.surface = surface

    # Updates this 'getting started' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event):
        pass

    # Draws the components of this 'getting started' screen.
    def draw(self):
        label = self.font.render("Hello World", 1, (255, 0, 0))
        self.surface.blit(label, (self.app.width / 2, self.app.height / 2))