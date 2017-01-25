import play.tile

class Grid:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height

        self.tile_width = 32
        self.tile_height = 32

        self.default_tile_color = (0, 0, 0)
        self.tiles = self.create_grid(grid_width, grid_height)

    # Constructs a matrix / grid of the given width and height
    def create_grid(self, width, height):
        tiles = {}
        for y in range(height):
            for x in range(width):
                tiles[(x, y)] = play.tile.Tile(x, y, self.tile_width, self.tile_height, self.default_tile_color)
        return tiles

    # Looks up a tile instance set at the specified coordinates.
    def get(self, x, y):
        return self.tiles[(x, y)]

    # Updates the state of this grid.
    def update(self):
        for tile in self.tiles.values():
            tile.update()

    # Handles an event.
    def on_event(self, event):
        pass

    # Draws the components of this grid.
    def draw(self, surface):
        for tile in self.tiles.values():
            tile.draw(surface)