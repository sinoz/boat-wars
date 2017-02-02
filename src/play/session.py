import play.player
import play.ship
import play.mine
import play.grid
import play.randomcard
import play.card as crd
import screens.sound as sound

import pygame
import math
import random

NoRangeDrawing = 0
DrawFireRange = 1
DrawMoveRange = 2

class Session:
    def __init__(self, language, grid, p1_name, p2_name):
        self.grid = grid
        self.language = language
        self.deck = play.randomcard.Cards()

        self.p1 = play.player.Player(self, p1_name)
        self.p2 = play.player.Player(self, p2_name)

        self.current_turn = self.p1

        self.turn_count = 0
        self.winner = None

        self.selected_ship = None

        self.selected_mine_card = None
        self.selected_ship_card = None

        self.amt_played_cards = 0

        self.mines = []

        self.draw_type = NoRangeDrawing
        self.add_initial_entities()

    # Adds the initial entities for this new session. Should only be called upon creation of a session.
    def add_initial_entities(self):
        # Adds four ships for player one
        self.p1.add_ship(play.ship.Ship(self.grid.get(5, 0), self.p1))
        self.p1.add_ship(play.ship.Ship(self.grid.get(10, 0), self.p1, type=play.ship.QueenMary))
        self.p1.add_ship(play.ship.Ship(self.grid.get(16, 0), self.p1, type=play.ship.Avenger))
        self.p1.add_ship(play.ship.Ship(self.grid.get(21, 0), self.p1))

        # And now we add four ships for player two
        self.p2.add_ship(play.ship.Ship(self.grid.get(5, 19), self.p2))
        self.p2.add_ship(play.ship.Ship(self.grid.get(10, 18), self.p2, type=play.ship.Avenger))
        self.p2.add_ship(play.ship.Ship(self.grid.get(16, 17), self.p2, type=play.ship.QueenMary))
        self.p2.add_ship(play.ship.Ship(self.grid.get(21, 19), self.p2))

        # Give 2 cards to player 1 and 2
        self.p1.add_card(crd.Card(self.deck.pick_currentdeck(), 'Normal', self.language))
        self.p1.add_card(crd.Card(self.deck.pick_currentdeck(), 'Normal', self.language))
        self.p2.add_card(crd.Card(self.deck.pick_currentdeck(), 'Normal', self.language))
        self.p2.add_card(crd.Card(self.deck.pick_currentdeck(), 'Normal', self.language))

        # Rotate the ships of player one to face the boats of player two
        self.p1.foreach_ship(lambda ship: ship.transform(180))

        # Add 9 mines to the playing field
        # Add 9 mines to the playing field at random locations on the grid.
        while len(self.mines) < 9:
            x = random.randint(0, self.grid.grid_width - 3)
            y = random.randint(3, self.grid.grid_height - 3)

            tile = self.grid.get(x, y)

            # If the random position landed on a ship or another mine, we skip the position
            # and continue generating..
            if not tile.ship is None or not tile.mine is None:
                continue

            self.mines.append(play.mine.Mine(self, self.grid.get(x, y)))

    # Switches between the fire range and move range drawing types, if applicable.
    def switch_draw_type(self):
        if not self.selected_ship is None and not self.selected_ship.in_defense_mode():
            if self.draw_type == DrawFireRange:
                self.draw_type = DrawMoveRange
            elif self.draw_type == DrawMoveRange:
                self.draw_type = DrawFireRange

    # Attempts to select a ship that is possibly located at the specified coordinates.
    def select_ship_if_present(self, x, y):
        for ship in self.current_turn.ships:
            occupied_tile_pos = ship.occupied_tile_pos(ship.in_attack_mode())
            for pos in occupied_tile_pos:
                if self.out_of_bounds(pos[0], pos[1]):
                    continue

                tile = self.grid.get(pos[0], pos[1])
                if tile.x == x and tile.y == y:
                    self.selected_ship = tile.ship
                    for pos in occupied_tile_pos:
                        if self.out_of_bounds(pos[0], pos[1]):
                            continue

                        tile = self.grid.get(pos[0], pos[1])
                        if not tile.ship is None:
                            if tile.ship.health == 0 or tile.ship.disabled:
                                continue

                            if not self.selected_ship_card is None and tile.ship.owner == self.current_turn:
                                tile.ship.apply_card_effect(self.selected_ship_card)
                                self.mark_ship_card_as_played()

                                return

                            self.selected_ship = tile.ship

                            if self.selected_ship.in_attack_mode():
                                self.draw_type = DrawMoveRange
                            else:
                                self.draw_type = DrawFireRange
                        tile.selected = True

    # Updates the state of a currently selected ship. Raises an `Exception` if no ship was selected
    # prior to this method call. Ensure to call `select_ship_if_present()` before calling this method.
    def update_selected_ship(self, click_tile_x, click_tile_y):
        if self.selected_ship is None:
            raise Exception("No ship was selected prior to this method call")

        r = 0
        if self.draw_type == DrawFireRange:
            r = self.selected_ship.firerange
        elif self.draw_type == DrawMoveRange:
            r = self.selected_ship.get_moverange()

        tiles = self.compute_range(self.selected_ship, r)
        for tile in tiles:
            if click_tile_x == tile.x and click_tile_y == tile.y:
                if self.draw_type == DrawMoveRange and not self.selected_ship.in_defense_mode() and not self.selected_ship.reached_move_limit():
                    occupied_tile_pos = self.selected_ship.occupied_tile_pos(self.selected_ship.in_attack_mode())
                    for pos in occupied_tile_pos:
                        if self.out_of_bounds(pos[0], pos[1]):
                            continue

                        tile = self.grid.get(pos[0], pos[1])
                        tile.set_ship(None)
                        sound.Plopperdeplop.tune(self, 'movement')

                    delta_x = click_tile_x - self.selected_ship.x
                    delta_y = click_tile_y - self.selected_ship.y

                    new_x = click_tile_x
                    new_y = click_tile_y

                    # To ensure ships move downwards by their tail instead of their head
                    if delta_y > 0:
                        # The y coordinate of the tail of the ship
                        tail_y = self.selected_ship.y + (self.selected_ship.size - 1)

                        # The distance between the tail and the destination
                        delta_y = click_tile_y - tail_y

                        # And finally to ensure ships move downwards by their tail instead of their head
                        new_y = (tail_y + delta_y) - (self.selected_ship.size - 1)

                        if new_y < 0:
                            new_y = 0

                    if delta_x < 0 or delta_x >= 1:
                        self.selected_ship.remaining_tiles -= int(math.fabs(delta_x))
                    elif delta_y < 0 or delta_y >= 1:
                        self.selected_ship.remaining_tiles -= int(math.fabs(delta_y))

                    if self.selected_ship.remaining_tiles < 0:
                        self.selected_ship.remaining_tiles = 0

                    # Finally update the position of the ship
                    self.selected_ship.update_pos(new_x, new_y)

                    occupied_tile_pos = self.selected_ship.occupied_tile_pos(self.selected_ship.in_attack_mode())
                    for pos in occupied_tile_pos:
                        if self.out_of_bounds(pos[0], pos[1]):
                            continue

                        tile = self.grid.get(pos[0], pos[1])
                        tile.set_ship(self.selected_ship)

                        # We take the last time a player has been awarded a special card and the current turn
                        last = self.selected_ship.last_special_card_turn
                        current = self.turn_count

                        # Now we calculate the delta between the current and last turn to decide whether to award the player
                        # with a special card.
                        turn_delta = int(math.fabs(current - last))

                        # Check if ship should receive special card
                        if len(self.current_turn.cards) < 6 and turn_delta > 3:
                            if self.current_turn == self.p1 and tile.y == 20:
                                self.current_turn.add_card(crd.Card(self.deck.pick_special(), 'Special', self.language))
                                self.selected_ship.last_special_card_turn = self.turn_count
                            elif self.current_turn == self.p2 and tile.y == 0:
                                self.current_turn.add_card(crd.Card(self.deck.pick_special(), 'Special', self.language))
                                self.selected_ship.last_special_card_turn = self.turn_count

                    break
                elif self.draw_type == DrawFireRange and not self.selected_ship.reached_fire_limit() and not self.selected_ship.remaining_tiles == 0 and not self.current_turn.reached_fire_limit():
                    tile = self.grid.get(click_tile_x, click_tile_y)
                    if not tile.ship is None:
                        self.fire(self.selected_ship, tile.ship)

        self.reset_ship_selection()
        self.reset_card_selection()

    # Attempts to select a mine that is possibly located at the specified coordinates.
    def select_mine_if_present(self, x, y):
        for mine in self.mines:
            tile = self.grid.get(x, y)
            if not tile.mine is None and x == mine.x and y == mine.y:
                if not self.selected_mine_card is None:
                    id = self.selected_mine_card.id
                    if id == 'son':
                        # Sonar deactivates a mine, we might as well remove it then
                        self.mines.remove(mine)
                        mine.clear()
                    elif id == 'navm':
                        # Remove the mine
                        self.mines.remove(mine)

                        # TODO: play explosion animation

                        target_ships = []
                        positions = tile.mine.get_surrounding_pos(3)
                        for pos in positions:
                            x = pos[0]
                            y = pos[1]

                            if x < 0 or y < 0 or x >= self.grid.grid_width or y >= self.grid.grid_height:
                                continue

                            tile = self.grid.get(x, y)
                            if not tile.ship is None and not tile.ship in target_ships:
                                target_ships.append(tile.ship)

                        mine.explode(target_ships)

                    self.mark_mine_card_as_played()

    # Marks the currently selected ship related card as played, incrementing the card play count, removing
    # the card from the player's deck and resetting any selected card.
    def mark_ship_card_as_played(self):
        self.amt_played_cards += 1
        self.current_turn.remove_card(self.selected_ship_card)

        # Trash current selected card
        if self.selected_ship_card.type == 'Normal':
            self.deck.trash_card(self.selected_ship_card.id)

        self.reset_card_selection()

    # Marks the currently selected mine related card as played, incrementing the card play count, removing
    # the card from the player's deck and resetting any selected card.
    def mark_mine_card_as_played(self):
        self.amt_played_cards += 1
        self.current_turn.remove_card(self.selected_mine_card)

        # Trash current selected card
        if self.selected_mine_card.type == 'Normal':
            self.deck.trash_card(self.selected_mine_card.id)

        self.reset_card_selection()

    # Draws the fire range of a ship
    def set_fire_range_drawing(self):
        tiles = self.compute_range(self.selected_ship, self.selected_ship.firerange)
        for tile in tiles:
            tile.with_fire_range = True
            tile.with_move_range = False

    # Draws the move range of a ship
    def set_move_range_drawing(self):
        tiles = self.compute_range(self.selected_ship, self.selected_ship.get_moverange())
        for tile in tiles:
            tile.with_fire_range = False
            tile.with_move_range = True

    # Computes a collection of tiles that are within the specified range
    def compute_range(self, ship, delta):
        if ship.in_attack_mode():
            return self.compute_attack_mode_range(ship, delta)
        else:
            return self.compute_defense_mode_range(ship, delta)

    # Computes a collection of tiles that are within the specified range assuming the given ship
    # is in attack mode.
    def compute_attack_mode_range(self, ship, delta):
        tiles = []

        y_offset = ship.y - delta
        y_end = (ship.y + ship.size + delta)

        for y in range(y_offset, y_end):
            occupied_tile_pos = ship.occupied_tile_pos(ship.in_attack_mode())
            for pos in occupied_tile_pos:
                if self.out_of_bounds(pos[0], pos[1]):
                    continue

                if ship.y == y or y == pos[1]:
                    continue

            if self.out_of_bounds(ship.x, y):
                continue

            tile = self.grid.get(ship.x, y)
            if not tile.ship is None:
                if ship.rect.colliderect(tile.ship.rect):
                    continue

                if self.draw_type == DrawFireRange and tile.ship.health == 0:
                    continue

                if self.draw_type == DrawFireRange and tile.ship.owner == self.current_turn:
                    continue

                elif self.draw_type == DrawMoveRange:
                    continue

            tiles.append(tile)

        y_offset = ship.y
        y_end = ship.y + ship.size

        for y in range(y_offset, y_end):
            start_x = (ship.x - delta)
            end_x = (ship.x + delta)

            x = start_x

            while x <= end_x:
                if ship.x == x:
                    x += 1
                    continue

                if self.out_of_bounds(x, y):
                    x += 1
                    continue

                tile = self.grid.get(x, y)
                if not tile.ship is None:
                    if ship.rect.colliderect(tile.ship.rect):
                        continue

                    if self.draw_type == DrawFireRange and tile.ship.health == 0:
                        x += 1
                        continue

                    if self.draw_type == DrawFireRange and tile.ship.owner == self.current_turn:
                        x += 1
                        continue

                    elif self.draw_type == DrawMoveRange:
                        x += 1
                        continue

                tiles.append(tile)
                x += 1
        return tiles

    # Computes a collection of tiles that are within the specified range assuming the given ship
    # is in defense mode.
    def compute_defense_mode_range(self, ship, delta):
        tiles = []

        y_offset = (ship.y - delta)
        y_end = (ship.y + ship.size + delta) - 1

        for y in range(y_offset, y_end):
            if self.out_of_bounds(ship.x, y):
                continue

            x_offset = ship.x
            x_end = (ship.x + ship.size)

            for x in range(x_offset, x_end):
                if self.out_of_bounds(x, y):
                    continue

                tile = self.grid.get(x, y)
                if not tile.ship is None:
                    if ship.rect.colliderect(tile.ship.rect):
                        continue

                    if self.draw_type == DrawFireRange and tile.ship.health == 0:
                        continue

                    if self.draw_type == DrawFireRange and tile.ship.owner == self.current_turn:
                        continue

                    elif self.draw_type == DrawMoveRange:
                        continue

                tiles.append(tile)

            y += 1
        return tiles

    # Executes an attack on the opponent ship, by the attacking ship. Subtracts the opponent ship's health
    # By the amount of firepower the attacking ship has.
    def fire(self, attacker, opponent):
        if not opponent.sabotage:
            if not opponent.applied_smokescreen:
                sound.Plopperdeplop.tune(self, attacker.cannon_sound)
                opponent.health -= attacker.firepower
            else:
                # TODO play smokescreen animation/sound
                opponent.applied_smokescreen = False
        else:
            # Do this before we call fire(), else we end up an infinite recursion
            opponent.sabotage = False

            self.fire(opponent, attacker)

        if attacker.emp:
            opponent.disabled = True

        if opponent.health <= 0:
            sound.Plopperdeplop.tune(self, 'explosion_ship')
            opponent.wreck()
            opponent.health = 0

        attacker.fire_count += 1 # Every ship can attack at most once
        attacker.owner.fire_count += 1 # A player can only attack two other ships per turn

        attacker.reset_attack_effects()

        if not opponent.owner.has_remaining_ships():
            self.winner = attacker.owner

    # Returns whether the specified coordinates are out of bounds.
    def out_of_bounds(self, x, y):
        if x < 0 or x >= self.grid.grid_width:
            return True

        if y < 0 or y >= self.grid.grid_height:
            return True

        return False

    # Resets the currently selected ship.
    def reset_ship_selection(self):
        self.selected_ship = None
        self.draw_type = NoRangeDrawing
        self.reset_tiles()

    # Resets the currently selected card.
    def reset_card_selection(self):
        self.selected_mine_card = None
        self.selected_ship_card = None

    # Resets the state of all of the tiles in the grid.
    def reset_tiles(self):
        self.grid.foreach_tile(lambda tile: tile.reset())

    # Changes the current turn to that of the specified player.
    def change_turn(self, p):
        # Give current player new card at end of turn
        if len(self.current_turn.cards) < 6:
            self.current_turn.add_card(crd.Card(self.deck.pick_currentdeck(), 'Normal', self.language))
        else:
            self.deck.trash_card(self.deck.pick_currentdeck())

        # Reset the fire and move counts
        p.foreach_ship(lambda ship: ship.reset_counts())
        p.fire_count = 0

        # Activates ships again if they had been disabled
        self.current_turn.foreach_ship(lambda ship: ship.reset_deactivation())

        # Reset the amount of played cards
        self.amt_played_cards = 0

        # Increment the turn count every time someone ends their turn
        self.turn_count += 1

        # Change current turn
        self.current_turn = p

    # Handles an input event.
    def on_event(self, event):
        # We do not handle any game input events if we've already declared a winner
        if not self.winner is None:
            return

        # Allows the user to switch between fire and move draw types through the `TAB` key.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            self.switch_draw_type()

        # Allows the user to select ships and perform actions upon selected ships
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            screen_x = mouse_pos[0]
            screen_y = mouse_pos[1]

            click_tile_x = int(screen_x / play.grid.TileWidth)
            click_tile_y = int(screen_y / play.grid.TileHeight)

            if click_tile_x < self.grid.grid_width and click_tile_y < self.grid.grid_height:
                self.reset_tiles()

                self.grid.foreach_tile(lambda tile: tile.reset())

                if self.selected_ship is None:
                    self.select_mine_if_present(click_tile_x, click_tile_y)
                    self.select_ship_if_present(click_tile_x, click_tile_y)
                else:
                    self.update_selected_ship(click_tile_x, click_tile_y)

                self.reset_card_selection()

        if not self.selected_ship is None:
            self.grid.foreach_tile(lambda tile: tile.reset())

            if self.draw_type == DrawFireRange:
                self.set_fire_range_drawing()
            elif self.draw_type == DrawMoveRange:
                self.set_move_range_drawing()

        self.grid.on_event(event)

    # Updates the state of this session.
    def update(self):
        self.p1.update()
        self.p2.update()
        self.grid.update()

    # Draws the grid and all of the players and their components
    def draw(self, surface):
        self.draw_mouse_tile_marking(surface)
        self.grid.draw(surface)
        self.draw_mines(surface)
        self.p1.draw(surface)
        self.p2.draw(surface)

    # Draws the marking that appears on a tile the mouse hovers over
    def draw_mouse_tile_marking(self, surface):
        mouse_pos = pygame.mouse.get_pos()

        click_x = mouse_pos[0]
        click_y = mouse_pos[1]

        grid_x = int(click_x / play.grid.TileWidth)
        grid_y = int(click_y / play.grid.TileHeight)

        if grid_x < self.grid.grid_width and grid_y < self.grid.grid_height:
            for tile in self.grid.tiles.values():
                tile.marked = False

            tile = self.grid.get(grid_x, grid_y)
            tile.marked = True

    # Draws all of the mines onto the given surface.
    def draw_mines(self, surface):
        self.foreach_mine(lambda mine: mine.draw(surface))

    # A foreach function that accepts a callback which takes a mine.
    def foreach_mine(self, f):
        for mine in self.mines:
            f(mine)
