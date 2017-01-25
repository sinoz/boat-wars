import play.player

class Session:
    def __init__(self, grid, p1_name, p2_name):
        self.grid = grid

        self.p1 = play.player.Player(self, p1_name)
        self.p2 = play.player.Player(self, p2_name)

    # Updates the state of this session.
    def update(self):
        self.p1.update()
        self.p2.update()
        self.grid.update()

    # Draws the grid and all of the players and their components
    def draw(self, surface):
        self.grid.draw(surface)
        self.p1.draw(surface)
        self.p2.draw(surface)