# A context to pass around other classes containing specific
# information regarding the application.
class AppContext:
    def __init__(self):
        self.title = "Boat Wars"

        # application resolution
        self.width = 1024
        self.height = 690

        # grid resolution
        self.grid_width = 20
        self.grid_height = 20