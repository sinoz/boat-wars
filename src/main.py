import pygame

from screens import MainScreen
from game import Game

# The resolution of the application frame
width = 500
height = 500

# Initializes pygame
pygame.init()

# We create a surface that will be set to the specified resolution
surface = pygame.display.set_mode((width, height))

# The screen to start the application with.
# NOTE: if you're working on a separate screen (such as hiscores, you can simply
# change the MainScreen() to your own implementation. Ensure however that your
# implementation contains the `update()` and `draw()` methods
screen = MainScreen()

# Creates the game and ignites the game loop
game = Game(surface, screen)
game.game_loop()