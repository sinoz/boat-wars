import pygame

import widget.button
import screens.game.cards

class GameScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/game/game.png')

        self.cards_button = widget.button.Button((890, 98), (113, 178), self.display_cards)
        self.attack_mode_button = widget.button.Button((887, 350), (119, 65), self.set_attack_mode)
        self.defense_mode_button = widget.button.Button((885, 432), (122, 68), self.set_defense_mode)
        self.end_turn_button = widget.button.Button((), (), self.end_turn)

    # Updates this 'game' screen.
    def update(self):
        self.game.grid.update()

    # Handles an event.
    def on_event(self, event):
        self.cards_button.on_event(event)
        self.attack_mode_button.on_event(event)
        self.defense_mode_button.on_event(event)
        self.end_turn_button.on_event(event)
        self.game.grid.on_event(event)

    # Ends the turn of the current player
    def end_turn(self, x, y, cursor):
        pass # TODO

    # Sets a boat to attack mode
    def set_attack_mode(self, x, y, cursor):
        pass # TODO

    # Sets a boat to defense mode
    def set_defense_mode(self, x, y, cursor):
        pass # TODO

    # Reacts to the user pressing on the 'cards' button
    def display_cards(self, x, y, cursor):
        self.game.set_screen(screens.game.cards.CardScreen(self.game, self))

    # Draws the components of this 'game' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))
        self.game.grid.draw()