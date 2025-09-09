import pygame
from tree import Tree
from config import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

tree = Tree()

print("DONE")

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,255))

    tree.draw(screen)
    tree.grow()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
