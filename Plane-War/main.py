import pygame
import sys
from codes import hero
from codes import enemies

pygame.init()
pygame.mixer.init()

n_smallEnemies = 8
n_middleEnemies = 4
n_bigEnemies = 1

background_size = (width, height) = (480, 640)
screen = pygame.display.set_mode(background_size)
pygame.display.set_caption("Plane-War")
pygame.display.set_icon(pygame.image.load("images/logo.png"))

background = pygame.image.load("images/background.png").convert()
background_music = pygame.mixer.music.load("sounds/background_music.mp3")
hero_fire_sound = pygame.mixer.Sound("sounds/hero_fire.wav")


def main():
    pygame.mixer.music.play(-1)

    # generate Hero
    Hero = hero.Hero(background_size)
    # generate Enemies
    Enemies = []
    for i in range(n_bigEnemies):
        Enemies.append(enemies.BigEnemy(background_size))
    for i in range(n_middleEnemies):
        Enemies.append(enemies.MiddleEnemy(background_size))
    for i in range(n_smallEnemies):
        Enemies.append(enemies.SmallEnemy(background_size))
    # bullets
    Bullets = []

    running = True
    fire_button_1 = False
    fire_button_2 = False
    frame_count = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pass

        # get keyboard action
        key_pressed = pygame.key.get_pressed()

        # deal keyboard action
        if key_pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        # hero move
        if not Hero.isAlive() and not frame_count % 18:
            Hero.destroy()
        else:
            if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
                Hero.moveUp()
            if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
                Hero.moveDown()
            if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
                Hero.moveLeft()
            if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
                Hero.moveRight()

        if not fire_button_1 and not fire_button_2:
            if key_pressed[pygame.K_j]:
                fire_button_1 = True
            if key_pressed[pygame.K_k]:
                fire_button_2 = True
            if fire_button_1 or fire_button_2:
                hero_fire_sound.play(-1)
        else:
            if not key_pressed[pygame.K_j]:
                fire_button_1 = False
            if not key_pressed[pygame.K_k]:
                fire_button_2 = False
            if not fire_button_1 and not fire_button_2:
                hero_fire_sound.fadeout(50)

        # hero shot
        if not frame_count % 6 and fire_button_1:
            Hero.shot_1(Bullets)
        if not frame_count % 8 and fire_button_2:
            Hero.shot_2(Bullets)

        # enemies move
        for eachEnemy in Enemies:
            if eachEnemy.lives > 0:
                eachEnemy.move()
            elif not frame_count % 12:
                eachEnemy.destroy()

        # bullets move
        for eachBullet in Bullets:
            eachBullet.move()

        # judge kill
        for eachEnemy in Enemies:
            # still alive
            if eachEnemy.lives > 0:
                if Hero.isAlive() and pygame.sprite.collide_mask(Hero, eachEnemy):
                    eachEnemy.destroy()
                    Hero.destroy()
                for eachBullet in Bullets:
                    if eachEnemy.rect.left <= eachBullet.rect.left \
                            and eachEnemy.rect.right >= eachBullet.rect.right:
                        if eachEnemy.rect.top <= eachBullet.rect.top \
                                and eachEnemy.rect.bottom >= eachBullet.rect.bottom:
                            eachEnemy.destroy(eachBullet.damage)
                            eachBullet.destroy()
            pass

        # switch image
        if not frame_count % 8:
            Hero.switchImage()
            for eachEnemy in Enemies:
                eachEnemy.switchImage()

        # draw background
        screen.blit(background, (0, 0))
        # draw hero
        screen.blit(Hero.image, Hero.rect)
        # draw enemies
        for eachEnemy in Enemies:
            screen.blit(eachEnemy.image, eachEnemy.rect)
        # dram bullets
        for eachBullet in Bullets:
            screen.blit(eachBullet.image, eachBullet.rect)
        
        pygame.display.flip()

        pygame.time.delay(1000 // 60)
        frame_count = (frame_count + 1) % 240
        pass

    pass


main()
