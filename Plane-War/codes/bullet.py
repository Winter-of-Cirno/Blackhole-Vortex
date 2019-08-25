import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, collection, damage, speed):
        self.image = image
        self.damage = damage
        self.collection = collection
        self.rect = self.image.get_rect()
        self.speed = speed

    def move(self):
        self.rect.top -= self.speed
        if self.rect.bottom <= -200:
            self.destroy()

    def destroy(self):
        self.collection.remove(self)
        del self
    pass


class Bullet_1(Bullet):
    def __init__(self, init_position, collection):
        Bullet.__init__(self,
                        pygame.image.load("images/bullet1.png").convert_alpha(),
                        collection, 3, 12)
        self.rect.left, self.rect.top = \
            int(init_position[0] - self.rect.width / 2), \
            int(init_position[1])
        pass
    pass


class Bullet_2(Bullet):
    def __init__(self, init_position, collection):
        Bullet.__init__(self,
                        pygame.image.load("images/bullet2.png").convert_alpha(),
                        collection, 2, 12)
        self.rect.left, self.rect.top = \
            int(init_position[0] - self.rect.width / 2), \
            int(init_position[1])
        pass
    pass
