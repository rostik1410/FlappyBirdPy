import random

import pygame


class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x, image):
        self.x = x
        self.height = 0
        self.gap = 100  # gap between top and bottom pipe
        self.img = image

        # where the top and bottom of the pipe is
        self.top = 0
        self.bottom = 0

        self.PIPE_TOP = pygame.transform.flip(self.img, False, True)
        self.PIPE_BOTTOM = self.img

        self.passed = False

        self.set_height()

    def set_height(self):
        """
        set the height of the pipe, from the top of the screen
        :return: None
        """
        self.height = random.randrange(50, 400)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def move(self):
        self.x -= self.VEL

    def collapse(self):
        pass