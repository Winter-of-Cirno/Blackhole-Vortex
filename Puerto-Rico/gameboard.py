from object import Object
from character import *
from player import *

class GameBoard(Object):
    def __init__(self):
        Object.__init__(self, "桌面", "游戏板", "游戏进行的主要区域")

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

        self.showInfo()

        pass

    def showInfo(self):
        print("角色卡情况\n")
        for eachCharacter in self.characters:
            eachCharacter.showInfo()
        print("玩家情况: \n")
        for eachPlayer in self.players:
            eachPlayer.showInfo()

    def selectCharacterPhase(self):
        print("请", self.currentPlayer.name, "选择角色:")
        number = int(input())
        self.currentPlayer.selectCharacter(self.characters[number])
        self.currentPlayer.character.selected()

    pass
