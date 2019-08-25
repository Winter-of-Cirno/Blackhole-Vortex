from character import Character
from building import Building

allItem = []

allItem.append(
    Character("拓荒者", "进行一个拓荒者阶段, "
        "结束后翻出新的种植园卡片",
                   "各个游戏者轮流获得一个种植园",
                   "可以不获得种植园而获得采石场")
)

allItem.append(
    Character("市长", "进行一个市长阶段, "
        "结束后将拓荒者放置到拓荒船上",
                   "各个游戏者轮流从拓荒船上获得一个拓荒者",
                   "可以从公共堆上额外获得一个拓荒者")
)

allItem.append(
    Character("建筑师", "进行一个建筑师阶段",
                   "各个游戏者轮流修建一个建筑物",
                   "少花费一个杜布隆")
)

allItem.append(
    Character("监管者", "进行一个监管者阶段",
                   "各个游戏者轮流从公共堆上获得一个与自己生产环节相应的货物",
                   "可以额外获得一个货物")
)

allItem.append(
    Character("商人", "进行一个商人阶段, "
        "结束后如果商会被填满, 清空商会",
                   "各个游戏者轮流向商会出售最多一个货物",
                   "出售时额外获得一个杜布隆")
)

allItem.append(
    Character("船长", "进行一个船长阶段, "
        "结束后清空装满货物的运输船",
                   "各个游戏者轮流将货物装上运输船",
                   "第一次装货时额外获得一个胜利分数")

)

allItem.append(
    Character("淘金者", "没有行动, 只有特权",
                   "无",
                   "从银行获得一个杜布隆")
)

allItem.append(
    Building("小型靛蓝作坊", "消耗靛蓝灌木, 制作染料", 1, 1, 1)
)

allItem.append(
    Building("靛蓝作坊", "消耗靛蓝灌木, 制作染料", 3, 3, 2)
)

allItem.append(
    Building("小型蔗糖磨坊", "消耗甘蔗, 制作蔗糖", 1, 2, 1)
)

allItem.append(
    Building("蔗糖磨坊", "消耗甘蔗, 制作蔗糖", 3, 4, 2)
)

print("波多黎各, 游戏介绍")
print()
for eachItem in allItem:
    eachItem.showInfo()
    print()
