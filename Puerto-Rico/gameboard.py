from object import Object
from character import *
from player import *
import random


class GameBoard(Object):
    def __init__(self):
        Object.__init__(self, "桌面", "游戏进行的主要区域")

        # set plantation cards
        self.plantationCards = \
            [CORN]*10 + [INDIGO]*12 + [CANE]*11 + \
            [TOBACCO]*9 + [COFFEE]*8
        random.shuffle(self.plantationCards)

        # set character cards
        self.characters = [
            Pioneer(0), Mayor(1), Architect(2), Supervisor(3),
            Merchant(4), Captain(5), GoldDigger(6), GoldDigger(7)
        ]

        # set players
        self.players = [
            Player(name="P1", number=1, money=3, governor=True),
            Player(name="P2", number=2, money=3, governor=False),
            Player(name="P3", number=3, money=3, governor=False),
            Player(name="P4", number=4, money=3, governor=False),
        ]
        self.players[0].buildSuburb(INDIGO)
        self.players[1].buildSuburb(INDIGO)
        self.players[2].buildSuburb(CORN)
        self.players[3].buildSuburb(CORN)
        self.turn = 0

        self.currentPlayer = self.players[self.turn]
        self.selectCharacterPhase()
        self.currentPlayer.character.act(self)

        self.showInfo()

        pass

    def showInfo(self):
        print("角色卡情况: \n")
        for eachCharacter in self.characters:
            eachCharacter.showInfo()
        print("玩家情况: \n")
        for eachPlayer in self.players:
            eachPlayer.showInfo()

    def showCharactersOption(self, charactersNumber):
        for eachCharacterNumber in charactersNumber:
            print(eachCharacterNumber, ":",
                  self.characters[eachCharacterNumber].name)
        pass

    def selectCharacterPhase(self):
        charactersNumber = []
        for eachCharacter in self.characters:
            if eachCharacter.enable:
                charactersNumber.append(eachCharacter.number)
        self.showCharactersOption(charactersNumber)
        number = self.currentPlayer.select("角色", charactersNumber)
        self.currentPlayer.selectCharacter(self.characters[number])
        self.currentPlayer.character.selected()

    pass
