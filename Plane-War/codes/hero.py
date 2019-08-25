import pygame
from codes import bullet


class Hero(pygame.sprite.Sprite):
    def __init__(self, background_size):
        pygame.sprite.Sprite.__init__(self)
        self.images = [
            pygame.image.load("images/me1.png").convert_alpha(),
            pygame.image.load("images/me2.png").convert_alpha(),
            pygame.image.load("images/me_destroy_1.png").convert_alpha(),
            pygame.image.load("images/me_destroy_2.png").convert_alpha(),
            pygame.image.load("images/me_destroy_3.png").convert_alpha(),
            pygame.image.load("images/me_destroy_4.png").convert_alpha()]
        self.index = 0
        self.speed = 4
        self.image = self.images[self.index]
        self.rect = self.images[0].get_rect()
        self.width, self.height = background_size[0], background_size[1]
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60
        pass

    def isAlive(self):
        return self.index == 0 or self.index == 1

    def moveUp(self):
        if self.rect.top >= 0 + self.speed:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom <= self.height - self.speed:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom = self.height

    def moveLeft(self):
        if self.rect.left >= 0 + self.speed:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right <= self.width - self.speed:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width

    def shot_1(self, Bullets):
        Bullets.append(bullet.Bullet_1(
            (self.rect.left + self.rect.width // 2, self.rect.top),
            Bullets))

    def shot_2(self, Bullets):
        Bullets.append(bullet.Bullet_2(
            (self.rect.left + self.rect.width // 5,
             self.rect.top + self.rect.height // 3),
            Bullets))
        Bullets.append(bullet.Bullet_2(
            (self.rect.left + self.rect.width * 4 // 5,
             self.rect.top + self.rect.height // 3),
            Bullets))

    def switchImage(self):
        if self.isAlive():
            self.index = not self.index
        self.image = self.images[self.index]

    def destroy(self):
        if self.isAlive():
            self.index = 2
        else:
            self.index += 1
        if self.index == 6:
            self.index = 0
            self.reset()
        self.image = self.images[self.index]

    def reset(self):
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60

    pass
