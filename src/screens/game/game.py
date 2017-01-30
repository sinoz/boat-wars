import pygame

import screens.game.cards
import screens.settings
import screens.sound as sound
import screens.termination
import screens.main_menu
import play.grid
import play.session
import widget.button
import play.ship

class GameScreen:
    def __init__(self, canvas, session):
        self.canvas = canvas
        self.session = session

        self.image = pygame.image.load('resources/screens/' + canvas.language + '/game/game.png')
        self.exit_image = pygame.image.load('resources/screens/' + canvas.language + '/game/ingame_exit.jpg')
        self.victory_image = pygame.image.load('resources/screens/' + canvas.language + '/game/victory.png')

        sound.Plopperdeplop.music(self, "battle_music")

        self.cards_button = widget.button.Button((890, 98), (113, 178), self.display_cards)
        self.attack_mode_button = widget.button.Button((887, 350), (119, 65), self.set_attack_mode)
        self.defense_mode_button = widget.button.Button((885, 432), (122, 68), self.set_defense_mode)
        self.end_turn_button = widget.button.Button((885, 608), (126, 79), self.end_turn)

        self.main_menu_button = widget.button.Button((338, 221), (318, 67), self.return_to_main_menu)
        self.vic_main_menu_button = widget.button.Button((333,365), (317,79), self.return_to_main_menu)
        self.settings_button = widget.button.Button((341, 301), (317, 65), self.return_to_settings)

        self.session.winner = None

        self.draw_exit = False
        self.draw_victory = False

        self.font = pygame.font.SysFont("monospace", 20, 1)

    # TODO
    def return_to_main_menu(self, x, y, cursor):
        self.canvas.set_screen(screens.main_menu.MainScreen(self.canvas))

    def return_to_settings(self, x, y, cursor):
        self.canvas.set_screen(screens.settings.SettingsScreen(self.canvas, self))

    # Updates this 'game' screen.
    def update(self):
        self.session.update()
        if self.session.winner != None:
            self.draw_victory = True
            if sound.current_song != 'victory':
                sound.Plopperdeplop.music(self, 'victory')

    # Handles an event.
    def on_event(self, event):
        if self.draw_exit:
            self.main_menu_button.on_event(event)
            self.settings_button.on_event(event)

        if self.draw_victory:
            self.vic_main_menu_button.on_event(event)

        self.cards_button.on_event(event)
        self.attack_mode_button.on_event(event)
        self.defense_mode_button.on_event(event)
        self.end_turn_button.on_event(event)
        self.session.on_event(event)

        if event.type == pygame.QUIT:
            self.canvas.set_screen(screens.termination.ExitScreen(self.canvas, self))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.draw_exit = not self.draw_exit

    # Ends the turn of the current player
    def end_turn(self, x, y, cursor):
        self.session.reset_card_selection()
        self.session.reset_ship_selection()

        if self.session.current_turn == self.session.p1:
            self.session.change_turn(self.session.p2)
        else:
            self.session.change_turn(self.session.p1)

    # Sets a boat to attack mode
    def set_attack_mode(self, x, y, cursor):
        if not self.session.selected_ship is None:
            # Look up the positions this ship would occupy if it were set in attack mode
            pos_in_atk_mode = self.session.selected_ship.occupied_tile_pos(True)
            for pos in pos_in_atk_mode:
                sound.Plopperdeplop.tune(self, 'change_mode')
                # If the ship is standing on the last tiles on the x axis, the ship would be
                # able to fall off the grid, hence the `return` to prevent switching to defense mode
                if self.session.out_of_bounds(pos[0], pos[1]):
                    return

                # Ignore our current exact position
                if pos[0] == self.session.selected_ship.x and pos[1] == self.session.selected_ship.y:
                    continue

                tile = self.session.grid.get(pos[0], pos[1])

                # If we're colliding with ANOTHER ship, we do not switch to defense mode
                if not tile.ship is None and not tile.ship is self.session.selected_ship:
                    return

            self.session.selected_ship.switch_attack_mode()

    # Sets a boat to defense mode
    def set_defense_mode(self, x, y, cursor):
        if not self.session.selected_ship is None:
            # Look up the positions this ship would occupy if it were set in defense mode
            pos_in_atk_mode = self.session.selected_ship.occupied_tile_pos(False)
            for pos in pos_in_atk_mode:
                sound.Plopperdeplop.tune(self, 'change_mode')
                # If the ship is standing on the last tiles on the x axis, the ship would be
                # able to fall off the grid, hence the `return` to prevent switching to defense mode
                if self.session.out_of_bounds(pos[0], pos[1]):
                    return

                # Ignore our current exact position
                if pos[0] == self.session.selected_ship.x and pos[1] == self.session.selected_ship.y:
                    continue

                tile = self.session.grid.get(pos[0], pos[1])

                # If we're colliding with ANOTHER ship, we do not switch to attack mode
                if not tile.ship is None and not tile.ship is self.session.selected_ship:
                    return

            if not self.session.selected_ship.reached_fire_limit():
                self.session.draw_type = play.session.DrawFireRange
            self.session.selected_ship.switch_defense_mode()

    # Reacts to the user pressing on the 'cards' button
    def display_cards(self, x, y, cursor):
        self.session.reset_card_selection()
        self.session.reset_ship_selection()
        self.session.reset_tiles()

        self.canvas.set_screen(screens.game.cards.CardScreen(self.canvas, self.session, self))

        sound.Plopperdeplop.tune(self, 'card_flip')

    # Draws the components of this 'game' screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))
        self.session.draw(surface)

        turn_display = self.font.render(str(self.session.current_turn.name), 1, (0, 0, 0))
        surface.blit(turn_display, (893, 22))
        if self.session.selected_ship is None:
            surface.blit(self.font.render("", 1, (0, 0, 0)), (891, 47))
        else:
            mode_display = self.font.render(self.session.selected_ship.mode_id_to_name(), 1, (0, 0, 0))
            surface.blit(mode_display, (906, 47))

        if self.draw_exit:
            x = (self.canvas.app.width / 2) - (540 / 2)
            y = (self.canvas.app.height / 2) - (340 / 2)

            surface.blit(self.exit_image, (x, y))

        if self.draw_victory:
            x = (self.canvas.app.width / 2) - (540 / 2)
            y = (self.canvas.app.height / 2) - (340 / 2)

            winner_display = self.font.render((str(self.session.winner.name) + ' Wins!'), 1, (0, 0, 0))
            self.font.set_bold(True)

            surface.blit(self.victory_image, (x, y))
            surface.blit(winner_display, (400, 267))