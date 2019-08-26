class Object:
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description

    def showInfo(self):
        print(self.name + ":", self.description)
    pass
