import play.ship

class Player:
    def __init__(self, session, name, ships=[]):
        self.session = session
        self.name = name
        self.score = 0
        self.ships = ships

        self.add_ship(play.ship.Ship(session.grid.get(10, 10)))
        self.add_ship(play.ship.Ship(session.grid.get(8, 16), type=play.ship.QueenMary))
        self.add_ship(play.ship.Ship(session.grid.get(19, 3), type=play.ship.Avenger))

    # Adds the given ship to this player's arsenal.
    def add_ship(self, ship):
        self.ships.append(ship)

    # Removes the specified ship from this player's arsenal.
    def remove_ship(self, ship):
        self.ships.remove(ship)

    # Updates the state of this player.
    def update(self):
        for ship in self.ships:
            ship.update()

    # Draws the components of this player.
    def draw(self, surface):
        for ship in self.ships:
            ship.draw(surface)