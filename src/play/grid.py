import play.tile
import pygame

class Grid:
    def __init__(self, surface, grid_width, grid_height):
        self.surface = surface

        self.grid_width = grid_width
        self.grid_height = grid_height

        self.tile_width = 16
        self.tile_height = 16

        self.tiles = self.create_grid(grid_width, grid_height)

    # Constructs a matrix / grid of the given width and height
    def create_grid(self, width, height):
        return [[play.tile.Tile() for y in range(width)] for x in range(height)]

    # Updates this play
    def update(self):
        pass

    # Handles an event
    def on_event(self, event):
        pass

    # Draws the components of this grid
    def draw(self):
        pass # TODO