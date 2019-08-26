from object import Object
from enumeration import *
from option import *


class Character(Object):
    def __init__(self, name, description, number, action, privilege):
        Object.__init__(self, name, description)
        self.number = number
        self.bounty = 0
        self.enable = True
        self.action = action
        self.privilege = privilege

    def showInfo(self):
        Object.showInfo(self)
        print("序号: " + str(self.number),
              "赏金: " + str(self.bounty),
              "可选择: " + str(self.enable))
        print()

    def introduction(self):
        Object.showInfo(self)
        print("行动: " + self.action)
        print("特权: " + self.privilege)

    def addBounty(self):
        self.bounty += 1

    def reset(self):
        self.enable = True

    def selected(self):
        self.enable = False
        self.bounty = 0
    pass


class Pioneer(Character):
    def __init__(self, number):
        Character.__init__(self, "拓荒者", "进行一个拓荒者阶段", number,
                           "各个游戏者轮流获得一个种植园",
                           "可以不获得种植园而获得采石场")

    def act(self, gameboard):
        # flip out 5 cards
        cards = gameboard.plantationCards[0:5]

        for i in range(N_PLAYERS):
            chooser = gameboard.players[(i + gameboard.turn) % N_PLAYERS]

            # pioneer or builder hut
            if i == 0 or chooser.existUrban(BUILDER_HUT):
                showSuburbOption(cards + [QUARRY])
                number = chooser.select("种植园或采石场", cards + [QUARRY])
            else:
                showSuburbOption(cards)
                number = chooser.select("种植园", cards)

            # remove card
            if number != QUARRY:
                cards.remove(number)
                gameboard.plantationCards.remove(number)

            # build
            chooser.buildSuburb(number)

        # remove card
        for eachCard in cards:
            gameboard.plantationCards.remove(eachCard)
    pass


class Mayor(Character):
    def __init__(self, number):
        Character.__init__(self, "市长", "进行一个市长阶段", number,
                           "各个游戏者轮流从拓荒船上获得一个拓荒者",
                           "可以从公共堆上额外获得一个拓荒者")
    pass


class Architect(Character):
    def __init__(self, number):
        Character.__init__(self, "建筑师", "进行一个建筑师阶段", number,
                           "各个游戏者轮流修建一个建筑物",
                           "少花费一个杜布隆")

    def act(self, gameboard):
        for i in range(N_PLAYERS):
            chooser = gameboard.players[(i + gameboard.turn) % N_PLAYERS]

            # architect or quarry
            discount = int(i == 0) + chooser.countQuarry()

            buildings = []
            for type in range(len(URBAN_BUILDING)):
                if not chooser.existUrban(type):
                    buildings.append(
                        (type, URBAN_BUILDING[type][P_NAME],
                         max(URBAN_BUILDING[type][P_PRICE] - discount, 0))
                    )

            showUrbanOption(buildings)
            number = chooser.select("建筑物", [row[0] for row in buildings])

            # build
            chooser.buildUrban(number)
    pass


class Supervisor(Character):
    def __init__(self, number):
        Character.__init__(self, "监管者", "进行一个监管者阶段", number,
                           "各个游戏者轮流获得一个与自己生产环节相应的货物",
                           "可以额外获得一个货物")
    pass


class Merchant(Character):
    def __init__(self, number):
        Character.__init__(self, "商人", "进行一个商人阶段", number,
                           "各个游戏者轮流向商会出售最多一个货物",
                           "出售时额外获得一个杜布隆")
    pass


class Captain(Character):
    def __init__(self, number):
        Character.__init__(self, "船长", "进行一个船长阶段", number,
                           "各个游戏者轮流将货物装上运输船",
                           "第一次装货时额外获得一个胜利分数")
    pass


class GoldDigger(Character):
    def __init__(self, number):
        Character.__init__(self, "淘金者", "没有行动只有特权", number,
                           "无",
                           "从银行获得一个杜布隆")

    def act(self, gameboard):
        gameboard.currentPlayer.addMoney(1)

    pass
