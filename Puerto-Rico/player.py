from object import Object
from area import *


class Player(Object):
    def __init__(self, name, number, money, governor):
        Object.__init__(self, name, "玩家", "游戏的操纵者")
        self.number = number
        self.money = money
        self.goods = [0, 0, 0, 0, 0]
        self.governor = governor
        self.character = None
        self.suburb = Suburb(number)
        self.urban = Urban(number)

    def showInfo(self):
        Object.showInfo(self)
        print("杜布隆:", self.money)
        print("玉米,染料,蔗糖,烟草叶,咖啡豆:", self.goods)
        print("总督:", self.governor)
        if self.character:
            print("角色:", self.character.name)
        else:
            print("角色:", "未选择")
        print()
        self.suburb.showInfo()
        print()
        self.urban.showInfo()
        print()

    def buildSuburb(self, type):
        self.suburb.build(type)

    def buildUrban(self, type):
        self.urban.build(type)

    def addMoney(self, number):
        self.money += number

    def addGoods(self, type, number):
        self.goods[type] += number

    def selectCharacter(self, character):
        self.character = character

    pass
