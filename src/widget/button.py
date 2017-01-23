import pygame
import screens.sound as sound

class Button:
    def __init__(self, point, dimension, listener):
        self.point = point
        self.dimension = dimension
        self.listener = listener

    def update(self):
        pass

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

            print(click_x, click_y)

            if click_x >= offset_x and click_y >= offset_y and click_x <= end_x and click_y <= end_y:
                sound.Plopperdeplop.tune(self, 'click')
                self.listener(click_x, click_y, mouse_cursor)

    def draw(self):
        pass