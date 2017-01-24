import play.tile
import pygame

class Grid:
    def __init__(self, surface, grid_width, grid_height):
        self.surface = surface

        self.grid_width = grid_width
        self.grid_height = grid_height

        self.tile_width = 32
        self.tile_height = 32

        self.tile_color = (0, 0, 0)

        self.draw_offset_x = 16
        self.draw_offset_y = 16

        self.tiles = self.create_grid(grid_width, grid_height)

    # Constructs a matrix / grid of the given width and height
    def create_grid(self, width, height):
        return [[play.tile.Tile() for y in range(width)] for x in range(height)]

    # Updates this grid
    def update(self):
        for tile_y in range(0, self.grid_height):
            for tile_x in range(0, self.grid_width):
                self.tiles[tile_y][tile_x].update()

    # Handles an event
    def on_event(self, event):
        pass

    # Draws the components of this grid
    def draw(self):
        for tile_y in range(0, self.grid_height):
            for tile_x in range(0, self.grid_width):
                x = self.draw_offset_x + (tile_x * self.tile_width)
                y = self.draw_offset_y + (tile_y * self.tile_height)

                pygame.draw.rect(self.surface, self.tile_color, (x, y, self.tile_width, self.tile_height), 1)