class Floor:
    VEL = 5

    def __init__(self, y, image: object):
        self.WIDTH = image.get_width()
        self.IMG = image
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def draw(self, win: object) -> None:
        """
        :param win:
        :return: None
        """
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))

    def move(self) -> None:
        """
        :return: None
        """
        self.x1 -= self.VEL
        self.x2 -= self.VEL
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        elif self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH
