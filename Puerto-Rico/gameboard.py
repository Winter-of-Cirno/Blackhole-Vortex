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

        # start
        while True:
            self.onRound()
        pass

    def showInfo(self):
        print("角色卡情况: \n")
        for eachCharacter in self.characters:
            eachCharacter.showInfo()
        print("玩家情况: \n")
        for eachPlayer in self.players:
            eachPlayer.showInfo()

    def oneTurn(self):
        # set currentPlayer
        self.currentPlayer = self.players[self.turn]

        # select character
        characters = []
        for eachCharacter in self.characters:
            if eachCharacter.enable:
                characters.append(
                    (eachCharacter.number,
                     eachCharacter.name,
                     eachCharacter.bounty)
                )

        showCharacterOption(characters)
        number = self.currentPlayer.select("角色", [row[0] for row in characters])
        self.currentPlayer.selectCharacter(self.characters[number])
        self.currentPlayer.character.selected()

        # act
        self.currentPlayer.character.act(self)

        # next turn
        self.turn = (self.turn + 1) % N_PLAYERS

        # show information
        self.showInfo()

    def onRound(self):
        # each player get a turn
        for i in range(N_PLAYERS):
            self.oneTurn()

        # add bounty
        for eachCharacter in self.characters:
            if eachCharacter.enable:
                eachCharacter.addBounty()
            else:
                eachCharacter.reset()
        pass
    pass
