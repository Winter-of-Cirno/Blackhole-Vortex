class Object:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def showInfo(self):
        print(self.name + ":", self.description)
    pass
