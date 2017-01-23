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
    def on_events(self, event):
        pass

    # Draws the components of this grid
    def draw(self):
        for tile_y in range(0, self.grid_height):
            for tile_x in range(0, self.grid_width):
                for pixel_y in range(0, self.tile_height):
                    for pixel_x in range(0, self.tile_width):
                        self.surface.set_at(((tile_x * pixel_x) + 100, (tile_y + pixel_y) + 100), pygame.Color(0, 255, 0))