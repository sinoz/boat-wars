import pygame

import db.db_service
import screens.sound as sound

import widget.button

HighscoresFetchQuery = "SELECT name, wins, losses, trim(from to_char(CAST(wins AS float) / CAST(wins + losses AS float), \'0.00\')) AS ratio FROM players GROUP BY name, wins, losses ORDER BY ratio DESC LIMIT 10;"
class HighscoresScreen: # TODO this needs optimization
    def __init__(self, canvas, prev=None):
        self.image = pygame.image.load('resources/screens/' + canvas.language + '/highscores.jpg')
        self.canvas = canvas
        self.prev = prev
        self.font = pygame.font.SysFont("monospace", 33, bold=True)
        self.return_button = widget.button.Button((16, 600), (93, 77), self.return_to_main)
        self.scores = db.db_service.query(HighscoresFetchQuery)
        self.color = (0, 0, 0)
        sound.Plopperdeplop.music(self, 'high_scores')

    # Draws the components of this highscores screen.
    def draw(self, surface):
        surface.blit(self.image, (0, 0))

        offset = 0
        count = 0
        column = 0

        for result in self.scores:
            if count == 5:
                count = 0
                offset = 0
                column += 1

            x = ((column * 530) + 147)
            y = (offset + 126)

            name = result[0]
            wins = result[1]
            losses = result[2]
            ratio = result[3]

            nameWinsLossesDisplay = self.font.render(str(name) + " " + str(wins) + "/" + str(losses), 1, self.color)
            ratioDisplay =  self.font.render("Ratio:" + str(ratio), 1, self.color)

            surface.blit(nameWinsLossesDisplay, (x, y))
            surface.blit(ratioDisplay, (x, y + 25))

            count += 1
            offset += 94

    # TODO
    def return_to_main(self, x, y, cursor):
        sound.Plopperdeplop.music(self, 'intro')
        self.canvas.set_screen(self.prev)

    # Handles an event.
    def on_event(self, event):
        self.return_button.on_event(event)

    # Updates this highscores screen.
    def update(self):
        pass