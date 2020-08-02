import os

import pygame

from bird import Bird
from floor import Floor
from pipe import Pipe

pygame.init()

WIN_WIDTH = 600
WIN_HEIGHT = 700
FLOOR = 630

STAT_FONT = pygame.font.SysFont("comicsans", 50)
END_FONT = pygame.font.SysFont("comicsans", 70)

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

    def draw_window(self, floor: Floor, bird: Bird, pipes: list, score: int) -> None:
        """
        drawing game objects
        :param floor:
        :param bird:
        :param pipes:
        :param score:
        :return: None
        """
        self.win.blit(bg_img, (0, 0))
        floor.draw(self.win)
        bird.draw(self.win)
        for pipe in pipes:
            pipe.draw(self.win)

        # score
        score_label = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
        self.win.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))

        pygame.display.update()

    def end_screen(self):
        """
        display an end screen when the player loses
        :return: None
        """
        run = True
        text_label = END_FONT.render("Press Space to Restart", 1, (255, 255, 255))
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    self.main()

            self.win.blit(text_label, (WIN_WIDTH / 2 - text_label.get_width() / 2, 500))
            pygame.display.update()

        pygame.quit()
        quit()

    def main(self) -> None:
        """
        do all game logic
        :return: None
        """
        run = True

        start = False
        lost = False
        score = 0
        floor = Floor(FLOOR, base_img)
        bird = Bird(100, 100, bird_images)
        pipes = [Pipe(600, pipe_img)]
        clock = pygame.time.Clock()
        while run:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
                    break

                if event.type == pygame.KEYDOWN and not lost:
                    if event.key == pygame.K_SPACE:
                        if not start:
                            start = True
                        bird.jump()

            if start:
                bird.move()
            if not lost:
                floor.move()

                if start:
                    rem = []
                    add_pipe = False
                    for pipe in pipes:
                        pipe.move()

                        if pipe.collide(bird):
                            lost = True

                        if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                            rem.append(pipe)

                        if not pipe.passed and pipe.x < bird.x:
                            pipe.passed = True
                            add_pipe = True

                    if add_pipe:
                        score += 1
                        pipes.append(Pipe(WIN_WIDTH, pipe_img))

                    for r in rem:
                        pipes.remove(r)

            if bird.y + bird_images[0].get_height() - 10 >= FLOOR:
                break

            self.draw_window(floor, bird, pipes, score)

        self.end_screen()
