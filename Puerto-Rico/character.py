from object import Object as Object


class Character(Object):
    def __init__(self, name, description, action, privilege):
        Object.__init__(self, name, "角色卡", description)
        self.action = action
        self.privilege = privilege

    def showInfo(self):
        Object.showInfo(self)
        print("行动: " + self.action)
        print("特权: " + self.privilege)

    pass

