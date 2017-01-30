import pygame

import widget.button

CardPositions = [(39, 46), (319, 47), (604, 46), (37, 330), (319, 329), (602, 326)]

class CardScreen:
    def __init__(self, canvas, session, prev=None):
        self.canvas = canvas
        self.session = session
        self.prev = prev
        self.image = pygame.image.load('resources/screens/' + canvas.language + '/game/cards.png')

        self.font = pygame.font.SysFont("monospace", 20, 1)
        self.return_button = widget.button.Button((41, 611), (90, 58), self.return_to_game)

        self.cards = []

        # This could've been done through a simple iteration but noo, python wants to suck so hard
        self.cards.append(widget.button.Button(CardPositions[0], (178, 240), lambda x, y, cursor: self.on_card(x, y, cursor, 0)))
        self.cards.append(widget.button.Button(CardPositions[1], (178, 240), lambda x, y, cursor: self.on_card(x, y, cursor, 1)))
        self.cards.append(widget.button.Button(CardPositions[2], (178, 240), lambda x, y, cursor: self.on_card(x, y, cursor, 2)))
        self.cards.append(widget.button.Button(CardPositions[3], (178, 240), lambda x, y, cursor: self.on_card(x, y, cursor, 3)))
        self.cards.append(widget.button.Button(CardPositions[4], (178, 240), lambda x, y, cursor: self.on_card(x, y, cursor, 4)))
        self.cards.append(widget.button.Button(CardPositions[5], (178, 240), lambda x, y, cursor: self.on_card(x, y, cursor, 5)))

    # TODO
    def on_card(self, x, y, cursor, id):
        # TODO
        self.canvas.set_screen(self.prev)

    # TODO
    def update(self):
        pass # TODO

    # Handles an event.
    def on_event(self, event):
        for card in self.cards:
            card.on_event(event)

        self.return_button.on_event(event)

    # Reacts to the user pressing on the return button
    def return_to_game(self, x, y, cursor):
        self.canvas.set_screen(self.prev)

    # Draws the components of the 'cards' screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))
        self.session.current_turn.draw_cards(surface)

        turn_display = self.font.render(str(self.session.current_turn.name), 1, (0, 0, 0))
        surface.blit(turn_display, (893, 35))