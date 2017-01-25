import play.player
import play.ship

class Session:
    def __init__(self, grid, p1_name, p2_name):
        self.grid = grid

        self.p1 = play.player.Player(self, p1_name)
        self.p2 = play.player.Player(self, p2_name)

        # Adds three ships for player one
        self.p1.add_ship(play.ship.Ship(grid.get(2, 2)))
        self.p1.add_ship(play.ship.Ship(grid.get(10, 1), type=play.ship.QueenMary))
        self.p1.add_ship(play.ship.Ship(grid.get(19, 1), type=play.ship.Avenger))

        # And now we add three ships for player two
        self.p2.add_ship(play.ship.Ship(grid.get(4, 16), type=play.ship.QueenMary))
        self.p2.add_ship(play.ship.Ship(grid.get(12, 14), type=play.ship.Avenger))
        self.p2.add_ship(play.ship.Ship(grid.get(17, 15)))

        # Rotate the ships of player one to face the boats of player two
        self.p1.forEachShip(lambda ship: ship.transform(180))

        # set some ships to defense mode
        grid.get(2, 2).ship.switch_defense_mode()
        grid.get(12, 14).ship.switch_defense_mode()

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