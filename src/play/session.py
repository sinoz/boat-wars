import play.player
import play.ship
import play.grid
import play.randomcard
import play.crd as crd
import screens.sound as sound

import pygame

NoRangeDrawing = 0
DrawFireRange = 1
DrawMoveRange = 2
# enemy = None

class Session:
    def __init__(self, language, grid, p1_name, p2_name):
        self.grid = grid
        self.language = language
        self.deck = play.randomcard.Cards()

        self.p1 = play.player.Player(self, p1_name)
        self.p2 = play.player.Player(self, p2_name)
        # self.enemy = play.player.Player.enemy(self)

        self.current_turn = self.p1
        self.selected_ship = None
        # self.selected_enemy_ship = None


        self.draw_type = NoRangeDrawing

        # Adds four ships for player one
        self.p1.add_ship(play.ship.Ship(grid.get(5, 0)))
        self.p1.add_ship(play.ship.Ship(grid.get(10, 0), type=play.ship.QueenMary))
        self.p1.add_ship(play.ship.Ship(grid.get(16, 0), type=play.ship.Avenger))
        self.p1.add_ship(play.ship.Ship(grid.get(21, 0)))

        # And now we add four ships for player two
        self.p2.add_ship(play.ship.Ship(grid.get(5, 19)))
        self.p2.add_ship(play.ship.Ship(grid.get(10, 18), type=play.ship.Avenger))
        self.p2.add_ship(play.ship.Ship(grid.get(16, 17), type=play.ship.QueenMary))
        self.p2.add_ship(play.ship.Ship(grid.get(21, 19)))

        # Give 2 cards to player 1 and 2
        self.p1.add_card(crd.Card(self.deck.pick_currentdeck(), 'Normal', self.language))
        self.p1.add_card(crd.Card(self.deck.pick_currentdeck(), 'Normal', self.language))
        self.p2.add_card(crd.Card(self.deck.pick_currentdeck(), 'Normal', self.language))
        self.p2.add_card(crd.Card(self.deck.pick_currentdeck(), 'Normal', self.language))

        # Rotate the ships of player one to face the boats of player two
        self.p1.forEachShip(lambda ship: ship.transform(180))

   # Handles an event.
    def on_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            if not self.selected_ship is None and not self.selected_ship.in_defense_mode():
                if self.draw_type == DrawFireRange:
                    self.draw_type = DrawMoveRange
                else:
                    self.draw_type = DrawFireRange

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            click_x = mouse_pos[0]
            click_y = mouse_pos[1]

            grid_x = int(click_x / play.grid.TileWidth)
            grid_y = int(click_y / play.grid.TileHeight)

            if grid_x < self.grid.grid_width and grid_y < self.grid.grid_height:
                if self.draw_type != DrawMoveRange:
                    self.reset_selection()
                self.reset_tiles()

                self.grid.forEachTile(lambda tile: tile.reset())

                if self.selected_ship is None:
                    for ship in self.current_turn.ships:
                        occupied_tile_pos = ship.occupied_tile_pos()
                        for pos in occupied_tile_pos:
                            tile = self.grid.get(pos[0], pos[1])
                            if tile.x == grid_x and tile.y == grid_y:
                                self.selected_ship = tile.ship
                                for pos in occupied_tile_pos:
                                    tile = self.grid.get(pos[0], pos[1])
                                    if not tile.ship is None:
                                        self.selected_ship = tile.ship
                                        self.draw_type = DrawFireRange
                                    tile.selected = True
                else:
                    r = 0
                    if self.draw_type == DrawFireRange:
                        r = self.selected_ship.firerange
                    elif self.draw_type == DrawMoveRange:
                        r = self.selected_ship.moverange

                    tiles = self.compute_range(self.selected_ship, r)
                    for tile in tiles:
                        if grid_x == tile.x and grid_y == tile.y:
                            if self.draw_type == DrawMoveRange and not self.selected_ship.in_defense_mode():
                                self.move_ship(self.selected_ship, grid_x, grid_y)
                                sound.Plopperdeplop.tune(self, 'movement')

                                break

                    self.selected_ship = None
                    self.draw_type = NoRangeDrawing

                    self.reset_selection()
                    self.reset_tiles()

        if not self.selected_ship is None:
            self.grid.forEachTile(lambda tile: tile.reset())

            if self.draw_type == DrawFireRange:
                self.draw_fire_range()
            elif self.draw_type == DrawMoveRange:
                self.draw_move_range()
        self.grid.on_event(event)

    # Draws the fire range of a ship
    def draw_fire_range(self):
        tiles = self.compute_range(self.selected_ship, self.selected_ship.firerange)
        for tile in tiles:
            tile.with_fire_range = True
            tile.with_move_range = False

    # Draws the move range of a ship
    def draw_move_range(self):
        tiles = self.compute_range(self.selected_ship, self.selected_ship.moverange)
        for tile in tiles:
            tile.with_fire_range = False
            tile.with_move_range = True

    # Computes a collection of tiles that are within the specified range
    def compute_range(self, ship, delta):
        if ship.in_attack_mode():
            return self.compute_attack_range(ship, delta)
        else:
            return self.compute_defense_range(ship, delta)

    # Computes a collection of tiles that are within the specified range assuming the given ship
    # is in attack mode.
    def compute_attack_range(self, ship, delta):
        tiles = []
        for y in range(ship.y - delta, (ship.y + ship.size + delta)):
            occupied_tile_pos = ship.occupied_tile_pos()
            for pos in occupied_tile_pos:
                if ship.y == y or y == pos[1]:
                    y += 1
                    continue

            if y < 0 or y >= self.grid.grid_height:
                y += 1
                continue

            tiles.append(self.grid.get(ship.x, y))
            y += 1

        for y in range(ship.y, ship.y + ship.size):
            start_x = (ship.x - delta)
            end_x = (ship.x + delta)

            x = start_x

            while x <= end_x:
                if ship.x == x:
                    x += 1
                    continue

                if x < 0 or x >= self.grid.grid_width or y < 0 or y >= self.grid.grid_height:
                    x += 1
                    continue

                tiles.append(self.grid.get(x, y))
                x += 1
        return tiles

    # Computes a collection of tiles that are within the specified range assuming the given ship
    # is in defense mode.
    def compute_defense_range(self, ship, delta):
        tiles = []

        y_offset = (ship.y - delta)
        y_end = (ship.y + ship.size + delta) - 1

        for y in range(y_offset, y_end):
            if y < 0 or y >= self.grid.grid_height or y == ship.y:
                continue

            x_offset = ship.x
            x_end = (ship.x + ship.size)

            for x in range(x_offset, x_end):
                if x < 0 or x >= self.grid.grid_width:
                    continue

                tiles.append(self.grid.get(x, y))

            y += 1
        return tiles

    # Resets the current selection of a ship.
    def reset_selection(self):
        self.draw_type = NoRangeDrawing
        self.selected_ship = None

    # Resets the state of all of the tiles in the grid.
    def reset_tiles(self):
        self.grid.forEachTile(lambda tile: tile.reset())

    # Updates the position from its current position to the specified position
    def move_ship(self, ship, x, y):
        if x < 0 or x >= self.grid.grid_width or y < 0 or y > self.grid.grid_height:
            return

        ship.x = x
        ship.y = y

        # Releases the ship from the tile the ship was standing on
        ship.tile.set_ship(None)

        # And assigns the ship to the new tile
        ship.tile = self.grid.get(x, y)
        ship.tile.set_ship(ship)

    # Changes the current turn to that of the specified player.
    def change_turn(self, p):

        # Give current player new card at end of turn
        if len(self.current_turn.cards) < 6:
            self.current_turn.add_card(crd.Card(self.deck.pick_currentdeck(), 'Normal', self.language))
        else:
            self.deck.trash_card(self.deck.pick_currentdeck())

        # Determine the enemy
        if self.current_turn == self.p1:
            self.p1.enemy = True
            self.p2.enemy = False
            self.current_turn = p
        elif self.current_turn == self.p2:
            self.p1.enemy = False
            self.p2.enemy = True
            self.current_turn = p

        # Change current turn
        # self.current_turn = p


    # Updates the state of this session.
    def update(self):
        self.p1.update()
        self.p2.update()
        self.grid.update()

    # Draws the grid and all of the players and their components
    def draw(self, surface):
        self.draw_mouse_tile_marking(surface)
        self.grid.draw(surface)
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

    # # Fire interaction between the ships
    # def battle(self,event):
    #     p2_boat_life = self.p2.session.selected_ship.Healthpoints
    #     p1_boat_firepower = self.p1.session.selected_ship.Firepower
    #
    #     if self.selected_ship != None:
    #         if self.session.selected_ship.mode == AttackMode:
    #             if self.tile.with_fire_range == True:
    #                 if event.type == pygame.MOUSEBUTTONDOWN:
    #                     if self.p2.session.selected_ship.tile != None:
    #                         self.p2_boat_life = p2_boat_life - p1_boat_firepower

            # # # # def selected_enemy_ship(self, event):
            # # # #     # if self.current_turn == self.p1:
            # # # #     #     if self.selected_ship is not None:
            # # # #     #         if event.type == pygame.MOUSEBUTTONDOWN and self.p2.enemy == True:
            # # # #     #             self.selected_enemy_ship = self.tile.ship
            # # # #
            # # # #
            # # # #         if self.selected__enemy_ship is None:
            # # # #                 for ship in self.current_turn.ships:
            # # #                     occupied_tile_pos = ship.occupied_tile_pos()
            # # #                     for pos in occupied_tile_pos:
            # # #                         tile = self.grid.get(pos[0], pos[1])
            # # #                         if tile.x == grid_x and tile.y == grid_y:
            # #                             self.selected_ship = tile.ship
            # #                             for pos in occupied_tile_pos:
            # #                                 tile = self.grid.get(pos[0], pos[1])
            # #                                 if not tile.ship is None:
            #                                     self.selected_ship = tile.ship
            #                                     self.draw_type = DrawFireRange
            #                                 tile.selected = True

