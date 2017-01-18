import pygame

class MainScreen:
    def __init__(self, app, surface):
        self.surface = surface
        self.image = pygame.image.load('resources/main_menu.jpg')
        self.app = app

    # Draws the components of this main menu screen.
    def draw(self):
        self.surface.blit(self.image, (0, 0))

    # Handles an event.
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_cursor = pygame.mouse.get_cursor()
            mouse_pos = pygame.mouse.get_pos()

            x = mouse_pos[0]
            y = mouse_pos[1]

            if x >= 350 and y >= 140 and x <= 670 and y <= 214:
                print("START GAME") # TODO
            elif x >= 354 and y >= 250 and x <= 668 and y <= 320:
                print("INSTRUCTIONS") # TODO
            elif x >= 359 and y >= 355 and x <= 670 and y <= 428:
                print("OPTIONS") # TODO
            elif x >= 356 and y >= 458 and x <= 667 and y <= 538:
                print("HIGHSCORES") # TODO

    # Updates this main menu screen.
    def update(self):
        pass