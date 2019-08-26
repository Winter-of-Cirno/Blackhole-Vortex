from enumeration import *


def showCharacterOption(characters):
    for eachCharacter in characters:
        print(str(eachCharacter[0]) + ":",
              eachCharacter[1],
              "(" + str(eachCharacter[2]) + ")")


def showSuburbOption(cards):
    for eachCard in cards:
        print(str(eachCard) + ":",
              SUBURB_BUILDING[eachCard][P_NAME])


def showUrbanOption(buildings):
    for eachBuilding in buildings:
        print(str(eachBuilding[0]) + ":",
              eachBuilding[1],
              "(" + str(eachBuilding[2]) + ")")
