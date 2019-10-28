import pygame


yR = 300
RED = (0, 255, 0)
xR = 0


class Barrier():
    def __init__(self, sc):
        self.sc = sc

    def draw(self, xR):
        pygame.draw.rect(self.sc, RED, (xR, yR, 30, 60))
