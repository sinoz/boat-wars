import pygame

from app import AppContext
from game import Game

from main_menu import MainScreen

# Initializes pygame
pygame.init()
pygame.font.init()

# The application context that is passed around the entire application.
# The context contains information about the application itself
app = AppContext()

# Configures the pygame application frame
pygame.display.set_caption(app.title)

# We create a surface that will be set to the specified resolution
surface = pygame.display.set_mode((app.width, app.height))

# The screen to start the application with.
# NOTE: if you're working on a separate screen (such as hiscores, you can simply
# change the MainScreen() to your own implementation. Ensure however that your
# implementation contains the `update()` and `draw()` methods
screen = MainScreen(app, surface)

# Creates the game and ignites the game loop
game = Game(surface, screen)
game.game_loop()

# The game loop has ended, let's de-initialize the pygame modules
pygame.quit()
pygame.font.quit()