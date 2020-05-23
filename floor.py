class Floor:
    VEL = 5

    def __init__(self, y, image):
        self.WIDTH = image.get_width()
        self.IMG = image
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        elif self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH
