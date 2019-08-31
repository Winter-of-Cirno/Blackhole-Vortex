import pygame
import sys
from game_panel import GamePanel
from common_panel import CommonPanel
from cursor import Cursor

SCREEN_SIZE = (1024, 768)
screen = pygame.display.set_mode(SCREEN_SIZE)
canvas = pygame.image.load("images/areas/canvas.png")
pygame.display.set_caption("Puerto-Rico")


def main():
    myGamePanel = GamePanel()
    myCommonPanel = CommonPanel()
    myCursor = Cursor(myGamePanel, myCommonPanel)

    while True:
        events = pygame.event.get()
        for eachEvent in events:
            if eachEvent.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif eachEvent.type == pygame.MOUSEBUTTONDOWN:
                myCursor.whenMouseButtonDown(eachEvent.pos)
                pass

        screen.blit(canvas, (0, 0))
        screen.blit(myGamePanel.genSurface(), (0, 0))
        screen.blit(myCommonPanel.genSurface(), (0, 0))
        pygame.display.flip()
        pygame.time.delay(200)

    pass


main()
