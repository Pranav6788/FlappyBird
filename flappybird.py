import pygame
from pygame.locals import *

pygame.init()

screen_width = 500
screen_height  = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy bird")

running = True

#background image
background = pygame.image.load("/Users/pranavsarvepalli/Downloads/flappybird_background.png")

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
