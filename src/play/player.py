class Player:
    def __init__(self, session, name):
        self.session = session
        self.name = name
        self.score = 0
        self.ships = []
        self.move_count = 0

    # Adds the given ship to this player's arsenal.
    def add_ship(self, ship):
        self.ships.append(ship)

    # Removes the specified ship from this player's arsenal.
    def remove_ship(self, ship):
        self.ships.remove(ship)

    # A foreach function that accepts a callback which takes a ship.
    def forEachShip(self, f):
        for ship in self.ships:
            f(ship)

    # Updates the state of this player.
    def update(self):
        self.forEachShip(lambda ship: ship.update())

    # Draws the components of this player.
    def draw(self, surface):
        self.forEachShip(lambda ship: ship.draw(surface))