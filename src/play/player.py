class Player:
    def __init__(self, session, name):
        self.session = session
        self.name = name
        self.score = 0
        self.ships = []
        self.cards = []
        self.fire_count = 0

    # Adds the given ship to this player's arsenal.
    def add_ship(self, ship):
        occupied_tile_pos = ship.occupied_tile_pos(ship.in_attack_mode())
        for pos in occupied_tile_pos:
            if self.session.out_of_bounds(pos[0], pos[1]):
                continue

            tile = self.session.grid.get(pos[0], pos[1])
            tile.set_ship(ship)

        self.ships.append(ship)

    # Removes the specified ship from this player's arsenal.
    def remove_ship(self, ship):
        occupied_tile_pos = ship.occupied_tile_pos(ship.in_attack_mode())
        for pos in occupied_tile_pos:
            if self.session.out_of_bounds(pos[0], pos[1]):
                continue

            tile = self.session.grid.get(pos[0], pos[1])
            tile.set_ship(None)

        self.ships.remove(ship)

    # Returns whether this player has any ships with remaining life points.
    def has_remaining_ships(self):
        has_remaining = False
        for ship in self.ships:
            if ship.health > 0:
                has_remaining = True
        return has_remaining

    # Returns whether this player has reached his/her attack limit.
    def reached_fire_limit(self):
        return self.fire_count == 2

    # A foreach function that accepts a callback which takes a ship.
    def foreach_ship(self, f):
        for ship in self.ships:
            f(ship)

    # Adds the given card to the player's normal stack
    def add_card(self, card):
        if len(self.cards) != 6:
            self.cards.append(card)

    # Removes specified card from player's normal stack
    def remove_card(self, card):
        self.cards.remove(card)

    # A foreach function that accepts a callback which takes a card.
    def foreach_card(self, f):
        x = 0
        for card in self.cards:
            f(card, x)
            x += 1

    # Updates the state of this player.
    def update(self):
        self.foreach_ship(lambda ship: ship.update())

    # Draws the cards of this player
    def draw_cards(self, surface):
        self.foreach_card(lambda card, x: card.draw(surface, x))

    # Draws the components of this player.
    def draw(self, surface):
        self.foreach_ship(lambda ship: ship.draw(surface))