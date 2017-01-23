import pygame

class TextField:
    def __init__(self, surface, point, dimension, color, text=""):
        self.surface = surface
        self.point = point
        self.dimension = dimension
        self.color = color
        self.font = pygame.font.SysFont("monospace", 30)
        self.text = text
        self.active = False

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

            self.active = click_x >= offset_x and click_y >= offset_y and click_x <= end_x and click_y <= end_y
        elif event.type == pygame.KEYDOWN:
            if event.key != pygame.K_BACKSPACE:
               self.add_character(chr(event.key))
            else:
                self.remove_character()

    def draw(self):
        label = self.font.render(self.text, 1, self.color)
        self.surface.blit(label, self.point)

    def add_character(self, character):
        self.text += character

    def remove_character(self):
        if len(self.text) > 0:
            self.text = self.text[0:len(self.text) - 1]

    def update(self):
        pass