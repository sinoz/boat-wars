import play.tile
import pygame
import random

class Grid:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height

        self.tile_width = 32
        self.tile_height = 32

        self.tile_color = (0, 0, 0)

        self.tiles = self.create_grid(grid_width, grid_height)

    def r_color(self):
        return (random.randint(30, 255),
                random.randint(30, 255),
                random.randint(30, 255))

    # Constructs a matrix / grid of the given width and height
    def create_grid(self, width, height):
        tiles = {}
        for y in range(height):
            for x in range(width):
                tiles[(x, y)] = play.tile.Tile(x, y, self.tile_width, self.tile_height, self.r_color())
        return tiles

    # Updates this grid
    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        world_x = int(mouse_x / self.grid_width)
        world_y = int(mouse_y / self.grid_height)

        print(world_x, world_y)

        for tile in self.tiles.values():
            tile.update()

    # Handles an event
    def on_event(self, event):
        pass

    # Draws the components of this grid
    def draw(self, surface):
        for tile in self.tiles.values():
            tile.draw(surface)