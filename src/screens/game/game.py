class GameScreen:
    def __init__(self, game):
        self.game = game

    # Updates this 'game' screen.
    def update(self):
        self.game.grid.update()

    # Handles an event.
    def on_event(self, event):
        self.game.grid.on_events(event)

    # Draws the components of this 'game' screen.
    def draw(self):
        self.game.grid.draw()