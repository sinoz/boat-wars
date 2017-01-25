class Session:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    # Updates the state of this session.
    def update(self):
        self.p1.update()
        self.p2.update()