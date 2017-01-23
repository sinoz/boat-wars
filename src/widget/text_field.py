import pygame

class TextField:
    def __init__(self, point, dimension):
        self.point = point
        self.dimension = dimension
        self.text = ""
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

    def draw(self):
        pass

    def update(self):
        pass