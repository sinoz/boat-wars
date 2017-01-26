import play.player
import play.ship
import play.grid
import play.randomcard

import pygame

class Session:
    def __init__(self, grid, p1_name, p2_name):
        self.grid = grid
        self.deck = play.randomcard.Cards()

        self.p1 = play.player.Player(self, p1_name)
        self.p2 = play.player.Player(self, p2_name)

        self.current_turn = self.p1
        self.selected_ship = None

        self.draw_type = 1

        # Adds three ships for player one
        self.p1.add_ship(play.ship.Ship(grid.get(2, 2)))
        self.p1.add_ship(play.ship.Ship(grid.get(10, 1), type=play.ship.QueenMary))
        self.p1.add_ship(play.ship.Ship(grid.get(4, 6), type=play.ship.Avenger))
        self.p1.add_ship(play.ship.Ship(grid.get(19, 1), type=play.ship.Avenger))

        # And now we add three ships for player two
        self.p2.add_ship(play.ship.Ship(grid.get(4, 16), type=play.ship.QueenMary))
        self.p2.add_ship(play.ship.Ship(grid.get(12, 14), type=play.ship.Avenger))
        self.p2.add_ship(play.ship.Ship(grid.get(7, 9), type=play.ship.Avenger))
        self.p2.add_ship(play.ship.Ship(grid.get(17, 15)))

        # Rotate the ships of player one to face the boats of player two
        self.p1.forEachShip(lambda ship: ship.transform(180))

        # set some ships to defense mode
        # grid.get(2, 2).ship.switch_defense_mode()
        grid.get(12, 14).ship.switch_defense_mode()

    # Handles an event.
    def on_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            if not self.selected_ship is None:
                if self.draw_type == 1:
                    self.draw_type = 2
                else:
                    self.draw_type = 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            click_x = mouse_pos[0]
            click_y = mouse_pos[1]

            grid_x = int(click_x / play.grid.TileWidth)
            grid_y = int(click_y / play.grid.TileHeight)

            self.reset_selection()

            if grid_x < self.grid.grid_width and grid_y < self.grid.grid_height:
                self.grid.forEachTile(lambda tile: tile.reset())

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
                                tile.selected = True

        if not self.selected_ship is None:
            self.grid.forEachTile(lambda tile: tile.reset())

            if self.draw_type == 1:
                self.draw_fire_range()
            elif self.draw_type == 2:
                self.draw_move_range()

        self.grid.on_event(event)

    # Draws the fire range of a ship
    def draw_fire_range(self):
        def f(tile):
            tile.with_move_range = False
            tile.with_fire_range = True

        self.draw_range(self.selected_ship, self.selected_ship.firerange, f)

    # Draws the move range of a ship
    def draw_move_range(self):
        def f(tile):
            tile.with_fire_range = False
            tile.with_move_range = True

        self.draw_range(self.selected_ship, self.selected_ship.moverange, f)

    # Draws a type of range for the specified ship.
    def draw_range(self, ship, r, f):
        if ship.in_attack_mode():
            for y in range(ship.y, ship.y + ship.size):
                start_x = (ship.x - r)
                end_x = (ship.x + r)

                x = start_x

                while x <= end_x:
                    if ship.x == x:
                        x += 1
                        continue

                    if x < 0 or x >= self.grid.grid_width or y < 0 or y >= self.grid.grid_height:
                        x += 1
                        continue

                    f(self.grid.get(x, y))
                    x += 1
        else:
            pass # TODO

    # Resets the current selected boat.
    def reset_selection(self):
        self.grid.forEachTile(lambda tile: tile.reset())
        self.selected_ship = None

    # Changes the current turn to that of the specified player.
    def change_turn(self, p):
        self.current_turn = p

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