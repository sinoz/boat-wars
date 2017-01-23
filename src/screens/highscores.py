import pygame

import screens.sound as sound
import widget.button
from db import db_service

HighscoresFetchQuery = 'SELECT name, score FROM players ORDER BY score DESC LIMIT 10;'

class HighscoresScreen:
    def __init__(self, game, prev=None):
        self.image = pygame.image.load('resources/screens/' + game.language + '/highscores.jpg')
        self.game = game
        self.prev = prev

        self.button = widget.button.Button((20, 604), (88, 72), self.return_to_prev)
        self.font = pygame.font.SysFont("monospace", 42)
        self.scores = db_service.query(HighscoresFetchQuery)

        sound.Plopperdeplop.music(self, 'high_scores')

        # The high scores music playing code
        pygame.mixer.music.load('resources/mp3/High_scores.mp3')
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(self.game.volume)

    # Draws the components of this highscores screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))

        offset = 0
        for result in self.scores:
            label = self.font.render(str(result[0]) + ":" + str(result[1]), 1, (0, 0, 0))
            self.game.surface.blit(label, (480, 190 + offset))
            offset += 78

    # Reacts to the user pressing on the return button
    def return_to_prev(self, x, y, cursor):
        sound.Plopperdeplop.tune(self, 'click')
        self.game.set_screen(self.prev)

    # Handles an event.
    def on_event(self, event):
        self.button.on_event(event)

    # Updates this highscores screen.
    def update(self):
        pass