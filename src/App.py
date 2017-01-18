import pygame

width = 500
height = 500

pygame.init()
screen = pygame.display.set_mode((width, height))

running = True

while running:
    # Wait for user events and react
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 255, 0)) # Green background
    pygame.display.flip() # Flips the graphics buffers to draw what's on the `screen`