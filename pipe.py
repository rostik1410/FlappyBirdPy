import random

import pygame


class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x, image: object):
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

    def set_height(self) -> None:
        """
        set the height of the pipe, from the top of the screen
        :return: None
        """
        self.height = random.randrange(50, 400)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def draw(self, win: object) -> None:
        """
        :param win:
        :return: None
        """
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def move(self) -> None:
        """
        :return: None
        """
        self.x -= self.VEL

    def collide(self, bird: object) -> bool:
        """
        check if bird collide with pipe
        :param bird:
        :return: boolean
        """
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if b_point or t_point:
            return True

        return False
