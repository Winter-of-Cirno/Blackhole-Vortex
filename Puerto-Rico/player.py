from object import Object
from area import *


class Player(Object):
    def __init__(self, name, number, money, governor):
        Object.__init__(self, name, "玩家")
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

    def select(self, string, scope):
        print("请", self.name, "选择", string)
        while True:
            number = int(input())
            if scope.count(number):
                break
            else:
                print("请重新选择")
        print()
        return number

    def buildSuburb(self, type):
        self.suburb.build(type)

    def buildUrban(self, type):
        self.urban.build(type)

    def countQuarry(self):
        count = 0
        for eachBuilding in self.suburb.buildingList:
            if eachBuilding.type == QUARRY:
                count += 1
        return count

    def existUrban(self, type):
        for eachBuilding in self.urban.buildingList:
            if eachBuilding.type == type:
                return True
        return False

    def addMoney(self, number):
        self.money += number

    def addGoods(self, type, number):
        self.goods[type] += number

    def selectCharacter(self, character):
        self.character = character

    pass
