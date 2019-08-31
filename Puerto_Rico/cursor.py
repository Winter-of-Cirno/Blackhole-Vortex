from enumeration import *
from game_panel import GamePanel
from common_panel import CommonPanel


class Cursor:
    def __init__(self, gp: GamePanel, cp: CommonPanel):
        self.gp = gp
        self.cp = cp
        self.moving = NOT_APPLICABLE
        self.movingType = NOT_APPLICABLE
        self.srcArea = NOT_APPLICABLE
        self.srcIndex = NOT_APPLICABLE

    def whenMouseButtonDown(self, position: tuple):
        ret = self.gp.whichArea(position)
        if ret[0] != NOT_APPLICABLE:
            print(ret)
        ret = self.cp.whichArea(position)
        if ret[0] != NOT_APPLICABLE:
            print(ret)
    pass
