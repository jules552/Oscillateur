import pygame, sys
from pygame.locals import *
from mass import Mass
from constants import *

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation")

run = True

clock = pygame.time.Clock()
dt = 0

point = Mass(100, 300, 0, 0.2)

while run:

    clock.tick(TICKRATES)
    win.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT or keys[pygame.K_END] or keys[pygame.K_DELETE]:
            run = False

    point.update(win, dt)

    pygame.display.update()

    dt += 0.02

pygame.quit()
sys.exit()
