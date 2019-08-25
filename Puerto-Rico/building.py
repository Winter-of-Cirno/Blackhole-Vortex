from object import Object


class Building(Object):
    def __init__(self, name, description,
                 n_workers, n_wins, n_price):
        Object.__init__(self, name, "建筑物", description)
        self.n_workers = n_workers
        self.n_wins = n_wins
        self.n_price = n_price

    def showInfo(self):
        Object.showInfo(self)
        print("岗位:", self.n_workers)
        print("胜点:", self.n_wins)
        print("价格:", self.n_price, "杜布隆")
    pass
