import pygame

class TextField:
    def __init__(self, game, point, dimension, color, maxLength, text=""):
        self.game = game
        self.point = point
        self.dimension = dimension
        self.color = color
        self.font = pygame.font.SysFont("monospace", 30)
        self.maxLength = maxLength
        self.text = text

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_cursor = pygame.mouse.get_cursor()
            mouse_pos = pygame.mouse.get_pos()

            click_x = mouse_pos[0]
            click_y = mouse_pos[1]

            offset_x = self.point[0]
            offset_y = self.point[1]

            end_x = offset_x + self.dimension[0]
            end_y = offset_y + self.dimension[1]

            if click_x >= offset_x and click_y >= offset_y and click_x <= end_x and click_y <= end_y:
                self.game.activeTextField = self
            else:
                self.game.activeTextField = None
        elif event.type == pygame.KEYDOWN and self.game.activeTextField is self:
            if event.key != pygame.K_BACKSPACE:
               self.add_character(chr(event.key))
            else:
                self.remove_character()

    def draw(self):
        label = self.font.render(self.text, 1, self.color)
        self.game.surface.blit(label, self.point)

    def add_character(self, character):
        if len(self.text) < self.maxLength:
            self.text += character

    def remove_character(self):
        if len(self.text) > 0:
            self.text = self.text[0:len(self.text) - 1]

    def update(self):
        pass