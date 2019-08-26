# general
N_PLAYERS = 4
N_PLANTATION = 5
N_PRODUCTION_BUILDINGS = 6
N_FUNCTION_BUILDING = 17

# location
SUBURB = 0
URBAN = 1

# plantation
CORN = 0
INDIGO = 1
CANE = 2
TOBACCO = 3
COFFEE = 4

# quarry
QUARRY = 5

# production building
SMAll_INDIGO_WORKSHOP = 0
SMAll_CANE_SUGAR_MILL = 1
INDIGO_WORKSHOP = 2
CANE_SUGAR_MILL = 3
TOBACCO_LIBRARY = 4
COFFEE_ROASTING_ROOM = 5

# function building
SMALL_MARKET_HALL = 6
FARMSTEAD = 7
BUILDER_HUT = 8
SMALL_WAREHOUSE = 9

ASYLUM = 10
TRIBUTARY_CHAMBER = 11
BIG_MARKET_HALL = 12
BIG_WAREHOUSE = 13

FACTORY = 14
UNIVERSITY = 15
HARBOR = 16
WHARF = 17

GUILD_HALL = 18
RESIDENCE = 19
FORTRESS = 20
CUSTOMS = 21
TOWN_HALL = 22

# names
CHARACTER_NAMES = [
    "拓荒者",
    "市长",
    "建筑师",
    "监管",
    "商人",
    "船长",
    "淘金者",
    "淘金者"
]

P_NAME = 0
P_DESCRIPTION = 1
P_MAX_WORKERS = 2
P_WINS = 3
P_PRICE = 4
P_AREA = 5

# suburb building
SUBURB_BUILDING = [
    ("玉米种植园", "产出玉米", 1, 0, 0, 1),
    ("靛蓝种植园", "产出靛蓝", 1, 0, 0, 1),
    ("甘蔗种植园", "产出甘蔗", 1, 0, 0, 1),
    ("烟草种植园", "产出烟草", 1, 0, 0, 1),
    ("咖啡种植园", "产出咖啡", 1, 0, 0, 1),
    ("采石场", "减少建筑物的价格", 1, 0, 0, 1)
]

# urban building
URBAN_BUILDING = [
    ("小型靛蓝作坊", "消耗靛蓝灌木制作染料", 1, 1, 1, 1),
    ("小型蔗糖磨坊", "消耗甘蔗制作蔗糖", 1, 2, 1, 1),
    ("靛蓝作坊", "消耗靛蓝灌木制作染料", 3, 3, 2, 1),
    ("蔗糖磨坊", "消耗甘蔗制作蔗糖", 3, 4, 2, 1),
    ("烟草库", "消耗烟草制作烟叶", 3, 5, 3, 1),
    ("咖啡烘培房", "消耗咖啡作物制作咖啡豆", 2, 6, 3, 1),
    ("小型市场大厅", "商人阶段出售货物时额外获得一个杜布隆", 1, 1, 1, 1),
    ("农庄", "拓荒者阶段可以额外获得一个暗置的种植园", 1, 2, 1, 1),
    ("建筑小屋", "拓荒者阶段可以选取一个采石场作为替代", 1, 2, 1, 1),
    ("小型仓库", "船长阶段可以额外存储一类货物", 1, 3, 1, 1),
    ("收容所", "拓荒者阶段选取郊区建筑后可以立即放置一个拓荒者", 1, 4, 2, 1),
    ("分商会", "商人阶段可以出售一种商会已有的货物", 1, 5, 2, 1),
    ("大型市场大厅", "商人阶段出售货物时额外获得两个杜布隆", 1, 5, 2, 1),
    ("大型仓库", "船长阶段可以额外存储两类货物", 1, 6, 2, 1),
    ("工厂", "监管阶段生产多类货物时可以获得额外的杜布隆", 1, 7, 3, 1),
    ("大学", "建筑师阶段选取城区建筑后可以立即放置一个拓荒者", 1, 8, 3, 1),
    ("港口", "船长阶段每次装载货物时都额外获得一个胜利分数", 1, 8, 3, 1),
    ("船坞", "船长阶段可以有一次机会直接将某类货物全部运送", 1, 9, 3, 1),
    ("公会大厅", "游戏结束时根据生产建筑的类型和数量额外获得胜利分数", 1, 10, 4, 2),
    ("官邸", "游戏结束时根据种植园和采石场的数量额外获得胜利分数", 1, 10, 4, 2),
    ("堡垒", "游戏结束时根据拓荒者的数量额外获得胜利分数", 1, 10, 4, 2),
    ("海关", "游戏结束时根据因船运获得的胜利分数额外获得胜利分数", 1, 10, 4, 2),
    ("市政厅", "游戏结束时根据功能建筑的数量额外获得胜利分数", 1, 10, 4, 2)
]