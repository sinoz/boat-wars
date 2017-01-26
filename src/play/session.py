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
        self.selected_ship = True

        # Adds three ships for player one
        self.p1.add_ship(play.ship.Ship(grid.get(2, 2)))
        self.p1.add_ship(play.ship.Ship(grid.get(10, 1), type=play.ship.QueenMary))
        self.p1.add_ship(play.ship.Ship(grid.get(4, 6), type=play.ship.Marejada))
        self.p1.add_ship(play.ship.Ship(grid.get(19, 1), type=play.ship.Avenger))

        # And now we add three ships for player two
        self.p2.add_ship(play.ship.Ship(grid.get(4, 16), type=play.ship.QueenMary))
        self.p2.add_ship(play.ship.Ship(grid.get(12, 14), type=play.ship.Avenger))
        self.p2.add_ship(play.ship.Ship(grid.get(7, 9), type=play.ship.Marejada))
        self.p2.add_ship(play.ship.Ship(grid.get(17, 15)))

        # Rotate the ships of player one to face the boats of player two
        self.p1.forEachShip(lambda ship: ship.transform(180))

        # set some ships to defense mode
        grid.get(2, 2).ship.switch_defense_mode()
        grid.get(12, 14).ship.switch_defense_mode()

    # Handles an event.
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            click_x = mouse_pos[0]
            click_y = mouse_pos[1]

            grid_x = int(click_x / play.grid.TileWidth)
            grid_y = int(click_y / play.grid.TileHeight)

            self.reset_selection()

            if grid_x < self.grid.grid_width and grid_y < self.grid.grid_height:
                for ship in self.current_turn.ships:
                    occupied_tile_pos = ship.occupied_tile_pos()
                    for pos in occupied_tile_pos:
                        tile = self.grid.get(pos[0], pos[1])
                        if tile.x == grid_x and tile.y == grid_y:
                            for pos in occupied_tile_pos:
                                tile = self.grid.get(pos[0], pos[1])
                                tile.selected = True

                            self.selected_ship = tile.ship
                            break

                # TODO set tile.selected to True if clicked on the boat
                # TODO set selected boat

        self.grid.on_event(event)

    # Resets the current selected boat.
    def reset_selection(self):
        self.grid.forEachTile(lambda tile: tile.reset_selection())
        self.selected_ship = None

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