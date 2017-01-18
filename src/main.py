import pygame

from screens import MainScreen
from game import Game

width = 500
height = 500

pygame.init()

surface = pygame.display.set_mode((width, height))

screen = MainScreen()
game = Game(surface, screen)

game.game_loop()