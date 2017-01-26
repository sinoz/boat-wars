import play.crd as crd

class Player:
    def __init__(self, session, name):
        self.session = session
        self.name = name
        self.score = 0
        self.ships = []
        self.cards = []

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

    # Adds the given card to the player's normal stack
    def add_card(self, card):
        self.cards.append(card)

    # Removes specified card from player's normal stack
    def remove_card(self, card):
        self.cards.remove(card)

    # A foreach function that accepts a callback which takes a card.
    def forEachCard(self, f):
        for card in self.cards:
            f(card)

    # Updates the state of this player.
    def update(self):
        self.forEachShip(lambda ship: ship.update())

    # Draws the cards of this player
    def draw_cards(self, surface):
        self.forEachCard(lambda card: crd.draw(surface))

    # Draws the components of this player.
    def draw(self, surface):
        self.forEachShip(lambda ship: ship.draw(surface))