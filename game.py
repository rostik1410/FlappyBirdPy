import os

import pygame

from bird import Bird
from floor import Floor
from pipe import Pipe

pygame.init()

WIN_WIDTH = 600
WIN_HEIGHT = 700
FLOOR = 630

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Test first py game :)')

base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")).convert_alpha())
bg_img = pygame.transform.scale(pygame.image.load(os.path.join("images", "bg.png")).convert_alpha(), (600, 700))
bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird" + str(x) + ".png"))) for x in
               range(1, 4)]
pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")).convert_alpha())


class Game:
    def __init__(self):
        self.win = WIN

    def draw_window(self, floor, bird, pipes):
        self.win.blit(bg_img, (0, 0))
        floor.draw(self.win)
        bird.draw(self.win)
        for pipe in pipes:
            pipe.draw(self.win)

        pygame.display.update()

    def main(self):
        run = True
        floor = Floor(FLOOR, base_img)
        bird = Bird(100, 100, bird_images)
        pipes = [Pipe(400, pipe_img)]
        clock = pygame.time.Clock()
        while run:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
                    break

            floor.move()

            rem = []
            add_pipe = False
            for pipe in pipes:
                pipe.move()

                if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                    rem.append(pipe)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if add_pipe:
                pipes.append(Pipe(WIN_WIDTH, pipe_img))

            for r in rem:
                pipes.remove(r)

            self.draw_window(floor, bird, pipes)
