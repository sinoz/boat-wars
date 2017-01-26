import play.tile

TileWidth = 32
TileHeight = 32

class Grid:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.tiles = self.create_grid(grid_width, grid_height)

    # Constructs a matrix / grid of the given width and height
    def create_grid(self, width, height):
        tiles = {}
        for y in range(height):
            for x in range(width):
                tiles[(x, y)] = play.tile.Tile(x, y, TileWidth, TileHeight)
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

    # A foreach function that accepts a callback which takes a tile.
    def forEachTile(self, f):
        for tile in self.tiles.values():
            f(tile)

    # Draws the components of this grid.
    def draw(self, surface):
        self.forEachTile(lambda tile: tile.draw(surface))