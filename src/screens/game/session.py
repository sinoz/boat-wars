import widget.text_field

class SessionScreen:
    def __init__(self, game):
        self.game = game
        self.p1_name = widget.text_field.TextField(game.surface, (100, 100), (250, 250), (0, 255, 0), "Typ iets dan")

    # Updates this 'session' screen.
    def update(self):
        pass # TODO

    # Handles an event.
    def on_event(self, event):
        self.p1_name.on_event(event)

    # Draws the components of this 'session' screen.
    def draw(self):
        self.p1_name.draw()