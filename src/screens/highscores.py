import pygame

from db import db_service
import screens.sound as sound

HighscoresFetchQuery = 'SELECT name, score FROM players ORDER BY score DESC LIMIT 10;'

class HighscoresScreen:
    def __init__(self, game):
        self.image = pygame.image.load('resources/screens/' + game.language + '/highscores.jpg')
        self.game = game
        self.font = pygame.font.SysFont("monospace", 42)
        self.scores = db_service.query(HighscoresFetchQuery)
        sound.Plopperdeplop.music(self, 'high_scores')

    # Draws the components of this highscores screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))

        offset = 0
        for result in self.scores:
            label = self.font.render(str(result[0]) + ":" + str(result[1]), 1, (0, 0, 0))
            self.game.surface.blit(label, (480, 190 + offset))
            offset += 78

    # Handles an event.
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_cursor = pygame.mouse.get_cursor()
            mouse_pos = pygame.mouse.get_pos()

            x = mouse_pos[0]
            y = mouse_pos[1]

            if x >= 413 and y >= 594 and x <= 646 and y <= 670:
                sound.Plopperdeplop.tune(self, 'click')
                from screens.main_menu import MainScreen
                self.game.set_screen(MainScreen(self.game))

    # Updates this highscores screen.
    def update(self):
        pass