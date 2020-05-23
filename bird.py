
class Bird:
    WIN_HEIGHT = 0
    WIN_WIDTH = 0
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y, images):
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

    def draw(self, win):
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

    def move(self):
        pass

    def jump(self):
        pass
