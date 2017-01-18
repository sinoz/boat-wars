import pygame

from main_menu import MainScreen
from game import Game

# The resolution of the application frame
width = 800
height = 600

# The title of the application frame
title = "Boat Wars"

# Initializes pygame
pygame.init()

# Configures the pygame application frame
pygame.display.set_caption(title)

# We create a surface that will be set to the specified resolution
surface = pygame.display.set_mode((width, height))

# Load all of our resources
main_menu_bg = pygame.image.load('resources/main_menu_bg.jpg')

# The screen to start the application with.
# NOTE: if you're working on a separate screen (such as hiscores, you can simply
# change the MainScreen() to your own implementation. Ensure however that your
# implementation contains the `update()` and `draw()` methods
screen = MainScreen(surface, main_menu_bg)

# Creates the game and ignites the game loop
game = Game(surface, screen)
game.game_loop()