class Player:
    def __init__(self, name, ships=[]):
        self.name = name
        self.score = 0
        self.ships = ships

    # Adds the given ship to this player's arsenal.
    def add_ship(self, ship):
        self.ships += ship

    # Removes the specified ship from this player's arsenal.
    def remove_ship(self, ship):
        self.ships -= ship

    # Updates the state of this player.
    def update(self):
        for ship in self.ships:
            ship.update()

    # Draws the components of this player.
    def draw(self, surface):
        for ship in self.ships:
            ship.draw()