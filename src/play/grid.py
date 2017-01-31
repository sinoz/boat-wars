import play.tile

TileWidth = 32
TileHeight = 32

class Grid:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height

        # Constructs the grid of size `grid_width` and `grid_height`
        self.tiles = {}
        for y in range(grid_height):
            for x in range(grid_width):
                self.tiles[(x, y)] = play.tile.Tile(x, y, TileWidth, TileHeight)

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

    # A foreach function that accepts a callback which takes a tile.
    def foreach_tile(self, f):
        for tile in self.tiles.values():
            f(tile)

    # Draws the components of this grid.
    def draw(self, surface):
        self.foreach_tile(lambda tile: tile.draw(surface))