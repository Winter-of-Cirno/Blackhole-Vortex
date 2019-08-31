import pygame
from enumeration import *


class Bank:
    def __init__(self):
        self.rect = pygame.Rect(BANK_POSITION, BANK_SIZE)
        self.image = pygame.image.load(IMAGE_BANK)

        self.blueprint: list[pygame.Rect] = []
        for i in range(len(SMALL_BUILDING_POSITIONS)):
            self.blueprint.append(pygame.Rect((SMALL_BUILDING_POSITIONS[i]), SMALL_BUILDING_SIZE))
        for i in range(len(BIG_BUILDING_POSITIONS)):
            self.blueprint.append(pygame.Rect((BIG_BUILDING_POSITIONS[i]), BIG_BUILDING_SIZE))

        self.vault = pygame.Rect(VAULT_POSITION, VAULT_SIZE)

        self.buildingImages: list[pygame.Surface] = []
        for i, eachItem in enumerate(URBAN_BUILDING):
            self.buildingImages.append(pygame.image.load(URBAN_BUILDING[i][5]))
        self.remaining: list[int] = SMALL_BUILDING_REMAINING + BIG_BUILDING_REMAINING

    def whichAreaBank(self, position: tuple) -> int:
        x = position[0] - self.rect.left
        y = position[1] - self.rect.top
        for i, eachBuilding in enumerate(self.blueprint):
            if eachBuilding.collidepoint(x, y):
                return i
        return NOT_APPLICABLE

    def addBuilding(self, type):
        self.remaining[type] += 1

    def subBuilding(self, type):
        self.remaining[type] -= 1

    def genSurface(self) -> pygame.Surface:
        background = self.image.copy()
        for i, eachNum in enumerate(self.remaining):
            if eachNum > 0:
                background.blit(
                    self.buildingImages[i],
                    (self.blueprint[i].left, self.blueprint[i].top)
                )
        return background

    pass


class Dock:
    def __init__(self):
        self.background = pygame.image.load(IMAGE_TRANSPARENCY)
        self.shipRects: list[pygame.Rect] = []
        for eachItem in SHIP_POSITIONS:
            self.shipRects.append(pygame.Rect(eachItem, SHIP_SIZE))
        self.shipImages: list[pygame.Surface] = [
            pygame.image.load(IMAGE_CARRIER_5),
            pygame.image.load(IMAGE_CARRIER_6),
            pygame.image.load(IMAGE_CARRIER_7)
        ]

    def whichAreaDock(self, position: tuple) -> int:
        # Dock have no Rect
        for i, eachShip in enumerate(self.shipRects):
            if eachShip.collidepoint(position):
                return i
        return NOT_APPLICABLE

    def genSurface(self) -> pygame.Surface:
        background = self.background.copy()
        for i, eachShip in enumerate(self.shipRects):
            background.blit(
                self.shipImages[i],
                (eachShip.left, eachShip.top)
            )
        return background

    pass


class Character:
    def __init__(self):
        self.background = pygame.image.load(IMAGE_TRANSPARENCY)
        self.image = pygame.image.load(IMAGE_CHARACTERS)
        self.position = CHARACTER_GROUP_POSITION

    def whichAreaCharacter(self, position: tuple) -> int:
        x = position[0] - self.position[0]
        y = position[1] - self.position[1]
        for i, eachItem in enumerate(CHARACTER_POSITIONS):
            if eachItem[0] <= x <= eachItem[0] + CHARACTER_SIZE[0]:
                if eachItem[1] <= y <= eachItem[1] + CHARACTER_SIZE[1]:
                    return i
        return NOT_APPLICABLE

    def genSurface(self) -> pygame.Surface:
        background = self.background.copy()
        # no bounty
        background.blit(self.image, self.position)
        return background
    pass


class CommonPanel:
    def __init__(self):
        self.background = pygame.image.load(IMAGE_TRANSPARENCY)
        self.bank = Bank()
        self.dock = Dock()
        self.character = Character()

    def genSurface(self) -> pygame.Surface:
        background = self.background.copy()
        background.blit(self.bank.genSurface(),
                        (self.bank.rect.left, self.bank.rect.top))
        background.blit(self.dock.genSurface(), (0, 0))
        background.blit(self.character.genSurface(), (0, 0))
        return background

    def whichArea(self, position: tuple) -> tuple:
        value = self.bank.whichAreaBank(position)
        if value != NOT_APPLICABLE:
            return AREA_BANK, value
        value = self.dock.whichAreaDock(position)
        if value != NOT_APPLICABLE:
            return AREA_DOCK, value
        value = self.character.whichAreaCharacter(position)
        if value != NOT_APPLICABLE:
            return AREA_CHARACTER, value
        return NOT_APPLICABLE, NOT_APPLICABLE

    pass
