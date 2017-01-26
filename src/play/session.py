import play.player
import play.ship
import play.grid
import play.randomcard

import pygame

NoRangeDrawing = 0
DrawFireRange = 1
DrawMoveRange = 2

AttackModeID = "Attack"
DefenseModeID = "Defense"
no_mode = "           "

class Session:
    def __init__(self, grid, p1_name, p2_name):
        self.grid = grid
        self.deck = play.randomcard.Cards()

        self.p1 = play.player.Player(self, p1_name)
        self.p2 = play.player.Player(self, p2_name)

        self.current_turn = self.p1
        self.selected_ship = None

        self.draw_type = NoRangeDrawing

        # Adds three ships for player one
        self.p1.add_ship(play.ship.Ship(grid.get(5, 0)))
        self.p1.add_ship(play.ship.Ship(grid.get(10, 0), type=play.ship.QueenMary))
        self.p1.add_ship(play.ship.Ship(grid.get(16, 0), type=play.ship.Avenger))
        self.p1.add_ship(play.ship.Ship(grid.get(21, 0)))

        # And now we add three ships for player two
        self.p2.add_ship(play.ship.Ship(grid.get(5, 19)))
        self.p2.add_ship(play.ship.Ship(grid.get(10, 18), type=play.ship.Avenger))
        self.p2.add_ship(play.ship.Ship(grid.get(16, 17), type=play.ship.QueenMary))
        self.p2.add_ship(play.ship.Ship(grid.get(21, 19)))

        # Rotate the ships of player one to face the boats of player two
        self.p1.forEachShip(lambda ship: ship.transform(180))

        # set some ships to defense mode
        # grid.get(2, 2).ship.switch_defense_mode()
        # grid.get(12, 14).ship.switch_defense_mode()

    # Handles an event.
    def on_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            if not self.selected_ship is None:
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

            self.reset_selection()

            if grid_x < self.grid.grid_width and grid_y < self.grid.grid_height:
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
                    pass # TODO move ship or fire other ship

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
    def compute_range(self, ship, r):
        tiles = []
        if ship.in_attack_mode():
            for y in range(ship.y - r, (ship.y + ship.size + r)):
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

                    tiles.append(self.grid.get(x, y))
                    x += 1
        else:
            pass # TODO
        return tiles

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
