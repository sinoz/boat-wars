import pygame

import screens.game.cards
import play.session
import widget.button
import screens.sound as sound

class GameScreen:
    def __init__(self, canvas, p1, p2):
        self.canvas = canvas
        self.session = play.session.Session(p1, p2)

        self.image = pygame.image.load('resources/screens/' + canvas.language + '/game/game.png')
        sound.Plopperdeplop.music(self, "battle_music")

        self.cards_button = widget.button.Button((890, 98), (113, 178), self.display_cards)
        self.attack_mode_button = widget.button.Button((887, 350), (119, 65), self.set_attack_mode)
        self.defense_mode_button = widget.button.Button((885, 432), (122, 68), self.set_defense_mode)
        self.end_turn_button = widget.button.Button((885, 608), (126, 79), self.end_turn)

    # Updates this 'game' screen.
    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        grid_x = int(mouse_x / self.canvas.grid.grid_width)
        grid_y = int(mouse_y / self.canvas.grid.grid_height)

        print(grid_x, grid_y)

        # TODO do something with grid coordinates

        self.session.update()
        self.canvas.grid.update()

    # Handles an event.
    def on_event(self, event):
        self.cards_button.on_event(event)
        self.attack_mode_button.on_event(event)
        self.defense_mode_button.on_event(event)
        self.end_turn_button.on_event(event)
        self.canvas.grid.on_event(event)

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
        self.canvas.set_screen(screens.game.cards.CardScreen(self.canvas, self))

    # Draws the components of this 'game' screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))
        self.canvas.grid.draw(surface)