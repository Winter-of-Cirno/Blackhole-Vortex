from object import Object
from building import *
from enumeration import *


class Area(Object):
    def __init__(self, name, description, number, capacity):
        Object.__init__(self, name, "区域", description)
        self.number = number
        self.buildingList = []
        self.size = 0
        self.capacity = capacity

    def showInfo(self):
        Object.showInfo(self)
        print("序号:", self.number)
        print("规模:", self.size)
        print("容量:", self.capacity)
        if self.size > 0:
            print("拥有:")
            for eachBuilding in self.buildingList:
                print("  ", eachBuilding.name)

    pass


class Suburb(Area):
    def __init__(self, number):
        Area.__init__(self, "郊区", "可以放置种植园和采石场", number, 12)

    def build(self, type):
        newBuilding = SuburbBuilding(type)
        self.buildingList.append(newBuilding)
        self.size += newBuilding.n_area
    pass


class Urban(Area):
    def __init__(self, number):
        Area.__init__(self, "城区", "可以放置生产建筑和功能建筑", number, 12)

    def build(self, type):
        newBuilding = UrbanBuilding(type)
        self.buildingList.append(newBuilding)
        self.size += newBuilding.n_area
    pass

