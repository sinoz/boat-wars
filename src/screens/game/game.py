import pygame

import screens.game.cards
import screens.sound as sound
import play.grid
import play.session
import widget.button
import play.ship


class GameScreen:
    def __init__(self, canvas, session):
        self.canvas = canvas
        self.session = session

        self.image = pygame.image.load('resources/screens/' + canvas.language + '/game/game.png')
        sound.Plopperdeplop.music(self, "battle_music")

        self.cards_button = widget.button.Button((890, 98), (113, 178), self.display_cards)
        self.attack_mode_button = widget.button.Button((887, 350), (119, 65), self.set_attack_mode)
        self.defense_mode_button = widget.button.Button((885, 432), (122, 68), self.set_defense_mode)
        self.end_turn_button = widget.button.Button((885, 608), (126, 79), self.end_turn)

        self.font = pygame.font.SysFont("monospace", 20)

    # Updates this 'game' screen.
    def update(self):
        self.session.update()

    # Handles an event.
    def on_event(self, event):
        self.cards_button.on_event(event)
        self.attack_mode_button.on_event(event)
        self.defense_mode_button.on_event(event)
        self.end_turn_button.on_event(event)
        self.session.on_event(event)

    # Ends the turn of the current player
    def end_turn(self, x, y, cursor):
        self.session.reset_selection()

        if self.session.current_turn == self.session.p1:
            self.session.change_turn(self.session.p2)
        else:
            self.session.change_turn(self.session.p1)

    # Sets a boat to attack mode
    def set_attack_mode(self, x, y, cursor):
        if not self.session.selected_ship is None:
            if not self.session.selected_ship.in_attack_mode():
                self.session.selected_ship.switch_attack_mode()

    # Sets a boat to defense mode
    def set_defense_mode(self, x, y, cursor):
        if not self.session.selected_ship is None:
            if not self.session.selected_ship.in_defense_mode():
                self.session.draw_type = play.session.DrawFireRange
                self.session.selected_ship.switch_defense_mode()

    # Reacts to the user pressing on the 'cards' button
    def display_cards(self, x, y, cursor):
        self.canvas.set_screen(screens.game.cards.CardScreen(self.canvas, self.session, self))

    # Draws the components of this 'game' screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))
        self.session.draw(surface)

        turn_display = self.font.render(str(self.session.current_turn.name), 1, (0, 0, 0))
        surface.blit(turn_display, (893, 22))
        if self.session.selected_ship is None:
            surface.blit(self.font.render("     ", 1, (0, 0, 0)), (891, 47))
        else:
            mode_display = self.font.render(self.session.selected_ship.mode_id_to_name(), 1, (0, 0, 0))
            surface.blit(mode_display, (906, 47))