class MainScreen:
    def __init__(self, surface, bgImage):
        self.surface = surface
        self.bgImage = bgImage

    # Draws the components of this main menu screen.
    def draw(self):
        self.surface.blit(self.bgImage, (0, 0))

    # Updates this main menu screen.
    def update(self):
        pass