import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, background_size, normal_images,
                 destroy_images, lives, speed):
        self.n_images = normal_images
        self.d_images = destroy_images
        self.lives = self.max_lives = lives
        self.speed = speed
        self.n_index, self.d_index = 0, 0
        self.image = self.n_images[self.n_index]
        self.rect = self.image.get_rect()
        self.width, self.height = background_size[0], background_size[1]

    def move(self):
        self.rect.bottom += self.speed
        if self.rect.bottom >= self.height + self.rect.height:
            self.reset()

    def switchImage(self):
        if self.lives > 0:
            self.n_index += 1
            if self.n_index == len(self.n_images):
                self.n_index = 0
            self.image = self.n_images[self.n_index]

    def destroy(self, damage=0):
        if self.lives > 0:
            self.lives -= damage
        if self.lives <= 0:
            if self.d_index == len(self.d_images):
                self.reset()
            else:
                self.image = self.d_images[self.d_index]
                self.d_index += 1

    def reset(self):
        self.lives = self.max_lives
        self.n_index, self.d_index = 0, 0
        self.image = self.n_images[self.n_index]
        self.rect.left, self.rect.top = \
            int(random.random() * (self.width - self.rect.width)), \
            int(random.random() * (-2) * self.height) - self.rect.height
    pass


class SmallEnemy(Enemy):
    def __init__(self, background_size):
        Enemy.__init__(self, background_size,
                       [pygame.image.load("images/enemy1.png").convert_alpha()],
                       [pygame.image.load("images/enemy1_down1.png").convert_alpha(),
                        pygame.image.load("images/enemy1_down2.png").convert_alpha(),
                        pygame.image.load("images/enemy1_down3.png").convert_alpha(),
                        pygame.image.load("images/enemy1_down4.png").convert_alpha()],
                       1, 3)
        self.reset()
        pass
    pass


class MiddleEnemy(Enemy):
    def __init__(self, background_size):
        Enemy.__init__(self, background_size,
                       [pygame.image.load("images/enemy2.png").convert_alpha()],
                       [pygame.image.load("images/enemy2_down1.png").convert_alpha(),
                        pygame.image.load("images/enemy2_down2.png").convert_alpha(),
                        pygame.image.load("images/enemy2_down3.png").convert_alpha(),
                        pygame.image.load("images/enemy2_down4.png").convert_alpha()],
                       12, 2)
        self.reset()
        pass
    pass


class BigEnemy(Enemy):
    def __init__(self, background_size):
        Enemy.__init__(self, background_size,
                       [pygame.image.load("images/enemy3_n1.png").convert_alpha(),
                        pygame.image.load("images/enemy3_n2.png").convert_alpha()],
                       [pygame.image.load("images/enemy3_down1.png").convert_alpha(),
                        pygame.image.load("images/enemy3_down2.png").convert_alpha(),
                        pygame.image.load("images/enemy3_down3.png").convert_alpha(),
                        pygame.image.load("images/enemy3_down4.png").convert_alpha(),
                        pygame.image.load("images/enemy3_down5.png").convert_alpha(),
                        pygame.image.load("images/enemy3_down6.png").convert_alpha()],
                       30, 1)
        self.reset()
        pass
    pass
