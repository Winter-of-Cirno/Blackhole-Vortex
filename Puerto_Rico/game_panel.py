import pygame
from enumeration import *


class PlayerPanel:
    def __init__(self, number: int, position: tuple):
        self.number = number
        self.rect = pygame.Rect(position, ME_PANEL_SIZE if number == 0 else OTHER_PANEL_SIZE)
        self.image = pygame.image.load(IMAGE_PLAYER_PANEL)
        self.urban: list[pygame.Rect] = []
        for i in range(len(URBAN_POSITIONS)):
            self.urban.append(pygame.Rect((URBAN_POSITIONS[i]), URBAN_SIZE))
        self.suburb: list[pygame.Rect] = []
        for i in range(len(SUBURB_POSITIONS)):
            self.suburb.append(pygame.Rect((SUBURB_POSITIONS[i]), SUBURB_SIZE))
        self.urbanZone: list[int] = [NOT_APPLICABLE] * len(URBAN_POSITIONS)
        # self.suburbZone: list[int] = [NOT_APPLICABLE] * len(SUBURB_POSITIONS)

    def addBuildingUrban(self, type, position):
        self.urbanZone[position] = type
        print(self.urbanZone)

    def whichAreaUrban(self, position: tuple) -> int:
        x = position[0] - self.rect.left
        y = position[1] - self.rect.top
        for i, eachBuilding in enumerate(self.urban):
            if eachBuilding.collidepoint(x, y):
                return i
        return NOT_APPLICABLE

    def whichAreaSuburb(self, position: tuple) -> int:
        x = position[0] - self.rect.left
        y = position[1] - self.rect.top
        for i, eachBuilding in enumerate(self.suburb):
            if eachBuilding.collidepoint(x, y):
                return i
        return NOT_APPLICABLE

    pass


class GamePanel:
    def __init__(self):
        self.panels = [
            PlayerPanel(0, PANEL_POSITIONS[0]),
            PlayerPanel(1, PANEL_POSITIONS[1]),
            PlayerPanel(2, PANEL_POSITIONS[2]),
            PlayerPanel(3, PANEL_POSITIONS[3])
        ]
        self.background = pygame.image.load(IMAGE_TRANSPARENCY)

    def genSurface(self) -> pygame.Surface:
        background = self.background.copy()
        background.blit(self.panels[0].image, (self.panels[0].rect.left, self.panels[0].rect.top))
        for eachPanel in self.panels[::-1][0:3]:
            background.blit(pygame.transform.scale(eachPanel.image, OTHER_PANEL_SIZE),
                            (eachPanel.rect.left, eachPanel.rect.top))
        return background

    def whichArea(self, position: tuple) -> tuple:
        value = self.panels[0].whichAreaUrban(position)
        if value != NOT_APPLICABLE:
            return AREA_URBAN, value
        value = self.panels[0].whichAreaSuburb(position)
        if value != NOT_APPLICABLE:
            return AREA_SUBURB, value
        return NOT_APPLICABLE, NOT_APPLICABLE

    pass
