from enum import Enum


class DungeonCardValues(Enum):
    MONSTER = 'monster'
    CHARACTER = 'character'
    WALL = 'wall'
    OBSTACLE = 'obstacle'
    TRAPS = 'trap'
    HAZARDOUS_TERRAIN = 'hazardous terrain'
    DIFFICULT_TERRAIN = 'difficult terrain'
    WALL_LINE = 'wall line'
    EMPTY = 'empty'
    COIN = 'coin'
    TREASURE = '5 gold'


class UniqueTileValues(Enum):
    pass


class UniqueDungeonCardValues(DungeonCardValues, UniqueTileValues):
    ENTRANCE_A = 'entrance a'
    ENTRANCE_B = 'entrance b'
    EXIT_A = 'exit a'
    EXIT_B = 'exit b'


class NumberedRoomTileValues(UniqueTileValues):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    ELEVEN = '11'
    TWELVE = '12'
