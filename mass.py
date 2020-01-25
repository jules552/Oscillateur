import pygame
import math
import scipy.constants
from constants import *


class Mass(object):
    def __init__(self, mass, length, s_angle, s_speed):
        self.x = length * math.cos(s_angle)
        self.y = length * math.sin(s_angle)
        self.m = mass
        self.L = length
        self.x_0 = s_angle
        self.v_0 = s_speed
        self.w = math.sqrt(scipy.constants.g / length)
        self.angle = s_angle

    def move(self, dt):
        self.angle = math.exp(-0.45/(2*self.m) * dt) * (self.x_0 * math.cos(self.w * dt) + (self.v_0 / self.w) * math.sin(
            self.w * dt)) + scipy.constants.pi / 2
        self.x = self.L * math.cos(self.angle) + WIDTH / 2
        self.y = self.L * math.sin(self.angle) + HEIGHT / 2

    def draw(self, win):
        for i in range(1, self.L):
            pygame.draw.rect(win, (255, 0, 0), (
                int(WIDTH / 2 + i * math.cos(self.angle)), int(HEIGHT / 2 + i * math.sin(self.angle)), 1, 3))
        pygame.draw.circle(win, (0, 255, 0), (int(self.x), int(self.y)), 5)
        pygame.draw.rect(win, (0, 0, 255), (0, int(HEIGHT / 2), WIDTH, 5), 0)

    def update(self, win, dt):
        self.move(dt)
        self.draw(win)
