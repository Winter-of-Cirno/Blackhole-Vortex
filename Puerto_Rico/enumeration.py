###
# Enumerate

# special
NOT_APPLICABLE = -1

# area
AREA_BANK = 0
AREA_DOCK = 1
AREA_CHARACTER = 2
AREA_URBAN = 3
AREA_SUBURB = 4

# type
TYPE_WORKER = 0
TYPE_GOODS = 1
TYPE_SUBURB = 2
TYPE_URBAN = 3

# urban building
SMALL_INDIGO_PLANT = 0
SMAll_SUGAR_MILL = 1
LARGE_INDIGO_PLANT = 2
SUGAR_MILL = 3
TOBACCO_BARN = 4
COFFEE_ROASTER = 5
SMALL_MARKET = 6
HACIENDA = 7
CONSTRUCTION_HUT = 8
SMALL_WAREHOUSE = 9
HOSPICE = 10
OFFICE = 11
LARGE_MARKET = 12
LARGE_WAREHOUSE = 13
FACTORY = 14
UNIVERSITY = 15
HARBOR = 16
WHARF = 17
GUILDHALL = 18
RESIDENCE = 19
FORTRESS = 20
CUSTOM_HOUSE = 21
CITY_HALL = 22

####
# Resource

# areas
IMAGE_TRANSPARENCY = "images/areas/transparency.png"
IMAGE_BANK = "images/areas/bank.png"
IMAGE_PLAYER_PANEL = "images/areas/player_panel.png"

# ships
IMAGE_CARRIER_5 = "images/ships/carrier_5.png"
IMAGE_CARRIER_6 = "images/ships/carrier_6.png"
IMAGE_CARRIER_7 = "images/ships/carrier_7.png"

# characters
IMAGE_CHARACTERS = "images/characters/characters.png"

# workers
IMAGE_WORKER = "images/items/worker.png"
IMAGE_WORKER_2 = "images/items/worker_2.png"
IMAGE_WORKER_3 = "images/items/worker_3.png"

# urban buildings
IMAGE_SMALL_INDIGO_PLANT = "images/buildings/0_small_indigo_plant.png"
IMAGE_SMAll_SUGAR_MILL = "images/buildings/1_small_sugar_mill.png"
IMAGE_LARGE_INDIGO_PLANT = "images/buildings/2_large_indigo_plant.png"
IMAGE_SUGAR_MILL = "images/buildings/3_large_sugar_mill.png"
IMAGE_TOBACCO_BARN = "images/buildings/4_tobacco_barn.png"
IMAGE_COFFEE_ROASTER = "images/buildings/5_coffee_roaster.png"
IMAGE_SMALL_MARKET = "images/buildings/6_small_market.png"
IMAGE_HACIENDA = "images/buildings/7_hacienda.png"
IMAGE_CONSTRUCTION_HUT = "images/buildings/8_construction_hut.png"
IMAGE_SMALL_WAREHOUSE = "images/buildings/9_small_warehouse.png"
IMAGE_HOSPICE = "images/buildings/10_hospice.png"
IMAGE_OFFICE = "images/buildings/11_office.png"
IMAGE_LARGE_MARKET = "images/buildings/11_large_market.png"
IMAGE_LARGE_WAREHOUSE = "images/buildings/12_large_warehouse.png"
IMAGE_FACTORY = "images/buildings/13_factory.png"
IMAGE_UNIVERSITY = "images/buildings/14_university.png"
IMAGE_HARBOR = "images/buildings/15_harbor.png"
IMAGE_WHARF = "images/buildings/16_wharf.png"

IMAGE_GUILDHALL = "images/buildings/17_guildhall.png"
IMAGE_RESIDENCE = "images/buildings/18_residence.png"
IMAGE_FORTRESS = "images/buildings/19_fortress.png"
IMAGE_CUSTOM_HOUSE = "images/buildings/20_custom_house.png"
IMAGE_CITY_HALL = "images/buildings/21_city_hall.png"

###
# Building (type, maxWorkers, wins, price, area, image)
URBAN_BUILDING = [
    (SMALL_INDIGO_PLANT, 1, 1, 1, 1, IMAGE_SMALL_INDIGO_PLANT),
    (SMAll_SUGAR_MILL, 1, 1, 2, 1, IMAGE_SMAll_SUGAR_MILL),
    (LARGE_INDIGO_PLANT, 3, 2, 3, 1, IMAGE_LARGE_INDIGO_PLANT),
    (SUGAR_MILL, 3, 2, 3, 1, IMAGE_SUGAR_MILL),
    (TOBACCO_BARN, 3, 3, 5, 1, IMAGE_TOBACCO_BARN),
    (COFFEE_ROASTER, 2, 3, 6, 1, IMAGE_COFFEE_ROASTER),

    (SMALL_MARKET, 1, 1, 1, 1, IMAGE_SMALL_MARKET),
    (HACIENDA, 1, 1, 2, 1, IMAGE_HACIENDA),
    (CONSTRUCTION_HUT, 1, 1, 2, 1, IMAGE_CONSTRUCTION_HUT),
    (SMALL_WAREHOUSE, 1, 1, 3, 1, IMAGE_SMALL_WAREHOUSE),

    (HOSPICE, 1, 2, 4, 1, IMAGE_HOSPICE),
    (OFFICE, 1, 2, 5, 1, IMAGE_OFFICE),
    (LARGE_MARKET, 1, 2, 5, 1, IMAGE_LARGE_MARKET),
    (LARGE_WAREHOUSE, 1, 2, 6, 1, IMAGE_LARGE_WAREHOUSE),

    (FACTORY, 1, 3, 7, 1, IMAGE_FACTORY),
    (UNIVERSITY, 1, 3, 8, 1, IMAGE_UNIVERSITY),
    (HARBOR, 1, 3, 8, 1, IMAGE_HARBOR),
    (WHARF, 1, 3, 9, 1, IMAGE_WHARF),

    (GUILDHALL, 1, 4, 10, 2, IMAGE_GUILDHALL),
    (RESIDENCE, 1, 4, 10, 2, IMAGE_RESIDENCE),
    (FORTRESS, 1, 4, 10, 2, IMAGE_FORTRESS),
    (CUSTOM_HOUSE, 1, 4, 10, 2, IMAGE_CUSTOM_HOUSE),
    (CITY_HALL, 1, 4, 10, 2, IMAGE_CITY_HALL),
]

###
# Common Panel

# Dock

SHIP_SIZE = (49, 90)
SHIP_POSITIONS = [
    (100, 50), (48, 95), (100, 150)
]

# Character

CHARACTER_GROUP_POSITION = (175, 475)
CHARACTER_SIZE = (50, 85)
CHARACTER_POSITIONS = [
    (2, 3), (68, 3), (134, 3), (200, 3),
    (2, 102), (68, 102), (134, 102)
]

# Bank

BANK_SIZE = (257, 358)
BANK_POSITION = (182, 58)

SMALL_BUILDING_SIZE = (50, 30)
SMALL_BUILDING_POSITIONS = [
    (17, 31), (17, 64),
    (74, 31), (74, 64),
    (131, 31), (131, 64),
    (17, 97), (17, 129), (17, 161), (17, 193),
    (74, 97), (74, 129), (74, 161), (74, 193),
    (131, 97), (131, 129), (131, 161), (131, 193)
]
SMALL_BUILDING_REMAINING = [
    4, 4,
    3, 3,
    3, 3,
    2, 2, 2, 2,
    2, 2, 2, 2,
    2, 2, 2, 2
]

BIG_BUILDING_SIZE = (50, 60)
BIG_BUILDING_POSITIONS = [
    (191, 32), (191, 95), (191, 158), (191, 221), (191, 284)
]
BIG_BUILDING_REMAINING = [
    1, 1, 1, 1, 1
]

VAULT_SIZE = (184, 107)
VAULT_POSITION = (25, 259)

###
# Game Panel

ME_PANEL_SIZE = (400, 270)
OTHER_PANEL_SIZE = (160, 108)
PANEL_POSITIONS = [(561, 406), (680, 110), (700, 93), (720, 76)]

URBAN_SIZE = (50, 30)
URBAN_POSITIONS = [
    (21, 144), (79, 144), (137, 144), (195, 144),
    (21, 177), (79, 177), (137, 177), (195, 177),
    (21, 210), (79, 210), (137, 210), (195, 210),
]

SUBURB_SIZE = (30, 28)
SUBURB_POSITIONS = [
    (56, 18), (111, 19), (164, 23), (209, 22),
    (61, 56), (104, 60), (156, 62), (215, 61),
    (61, 93), (104, 101), (162, 100), (208, 99)
]
