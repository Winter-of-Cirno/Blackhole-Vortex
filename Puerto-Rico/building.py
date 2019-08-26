from object import Object
from enumeration import *


class Building(Object):
    def __init__(self, name, description, type,
                 n_maxWorkers, n_wins, n_price, n_area):
        Object.__init__(self, name, description)
        self.type = type
        self.n_maxWorkers = n_maxWorkers
        self.n_workers = 0
        self.n_wins = n_wins
        self.n_price = n_price
        self.n_area = n_area

    def showInfo(self):
        Object.showInfo(self)
        print("岗位:", self.n_maxWorkers,
              "工人:", self.n_workers)
        print("胜点:", self.n_wins,
              "价格:", self.n_price,
              "面积:", self.n_area)

    def isFull(self):
        return self.n_workers == self.n_maxWorkers

    def isEmpty(self):
        return self.n_workers == 0

    def addWorker(self):
        self.n_workers += 1

    def subWorker(self):
        self.n_workers -= 1

    def workers(self):
        return self.n_workers
    pass


class SuburbBuilding(Building):
    def __init__(self, type):
        name, description, n_maxWorkers, n_wins, n_price, n_area = SUBURB_BUILDING[type]
        Building.__init__(self, name, description, type, n_maxWorkers, n_wins, n_price, n_area)

        if type <= N_PLANTATION:
            self.plantation = True
        else:
            self.plantation = False
    pass


class UrbanBuilding(Building):
    def __init__(self, type):
        name, description, n_maxWorkers, n_wins, n_price, n_area = URBAN_BUILDING[type]

        Building.__init__(self, name, description, type, n_maxWorkers, n_wins, n_price, n_area)

        if type <= N_PRODUCTION_BUILDINGS:
            self.productionBuilding = True
        else:
            self.productionBuilding = False
    pass
