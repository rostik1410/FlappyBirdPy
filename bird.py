import pygame


class Bird:
    WIN_HEIGHT = 0
    WIN_WIDTH = 0
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x: int, y: int, images: list):
        self.x = x
        self.y = y
        self.gravity = 9.8
        self.tilt = 0  # degrees to tilt
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.IMAGES = images
        self.IMG = self.IMAGES[0]

    def draw(self, win: object) -> None:
        """
        :return: None
        :param win: 
        """
        self.img_count += 1

        # For animation of bird, loop through three images
        if self.img_count <= self.ANIMATION_TIME:
            self.IMG = self.IMAGES[0]
        elif self.img_count <= self.ANIMATION_TIME * 2:
            self.IMG = self.IMAGES[1]
        elif self.img_count <= self.ANIMATION_TIME * 3:
            self.IMG = self.IMAGES[2]
        elif self.img_count <= self.ANIMATION_TIME * 4:
            self.IMG = self.IMAGES[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.IMG = self.IMAGES[0]
            self.img_count = 0

        win.blit(self.IMG, (self.x, self.y))

    def jump(self) -> None:
        """
        :return: None
        """
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self) -> None:
        """
        :return: None
        """
        self.tick_count += 1

        # for downward acceleration
        displacement = self.vel * (self.tick_count) + 0.5 * (3) * (self.tick_count) ** 2  # calculate displacement

        # terminal velocity
        if displacement >= 16:
            displacement = (displacement / abs(displacement)) * 16

        if displacement < 0:
            displacement -= 2

        self.y = self.y + displacement

        if displacement < 0 or self.y < self.height + 50:  # tilt up
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:  # tilt down
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def get_mask(self) -> object:
        """
        :return: Pygame object
        """
        return pygame.mask.from_surface(self.IMG)

