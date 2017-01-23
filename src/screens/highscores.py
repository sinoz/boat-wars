import pygame

import db.db_service
import screens.sound as sound

import widget.button

HighscoresFetchQuery = 'SELECT name, score FROM players ORDER BY score DESC LIMIT 10;'

class HighscoresScreen:
    def __init__(self, game, prev=None):
        self.image = pygame.image.load('resources/screens/' + game.language + '/highscores.jpg')
        self.game = game
        self.prev = prev
        self.font = pygame.font.SysFont("monospace", 42)
        self.return_button = widget.button.Button((16, 600), (93, 77), self.return_to_main)
        self.scores = db.db_service.query(HighscoresFetchQuery)
        self.play_music()

    # Plays the appropriate music for this screen
    def play_music(self):
        sound.Plopperdeplop.music(self, 'high_scores')

    # Draws the components of this highscores screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))

        offset = 0
        for result in self.scores:
            label = self.font.render(str(result[0]) + ":" + str(result[1]), 1, (0, 0, 0))
            self.game.surface.blit(label, (480, 190 + offset))
            offset += 78

    # TODO
    def return_to_main(self, x, y, cursor):
        sound.Plopperdeplop.music(self, 'intro')
        self.game.set_screen(self.prev)

    # Handles an event.
    def on_event(self, event):
        self.return_button.on_event(event)

    # Updates this highscores screen.
    def update(self):
        pass