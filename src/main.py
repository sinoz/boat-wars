import pygame

from app import AppContext
from game import Game

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

# Creates the game and ignites the game loop
game = Game(app, surface)
game.game_loop()

# The game loop has ended, let's de-initialize the pygame modules
pygame.quit()
pygame.font.quit()