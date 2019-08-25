import os


def file_name(file_dir):  
    L = []
    for root, dirs, files in os.walk(file_dir): 
        for file in files: 
            if os.path.splitext(file)[1] == '.png':
                L.append(file)
    return L 


names = file_name(r"D:\Git\Games\PlaneWar\images\\")

import pygame

pygame.init()
pygame.display.set_mode()

for name in names:
    image = pygame.image.load(name).convert_alpha()
    pygame.image.save(image, name)