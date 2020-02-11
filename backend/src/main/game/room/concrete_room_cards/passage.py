from backend.src.main.game.monster.values import (
    DungeonCardValues,
    NumberedRoomTileValues,
    UniqueDungeonCardValues)
from backend.src.main.game.room.abstract_room_card import AbstractRoomCard


class Passage(AbstractRoomCard):

    def __init__(self):
        AbstractRoomCard.__init__(self, "Passage")
        self.add_tile(NumberedRoomTileValues.TEN, -2, -1)
        self.add_tile(DungeonCardValues.OBSTACLE, -2, 0)
        self.add_tile(DungeonCardValues.OBSTACLE, -2, 1)
        self.add_tile(DungeonCardValues.EMPTY, -2, -2)
        self.add_tile(NumberedRoomTileValues.ELEVEN, -1, -2)
        self.add_tile(DungeonCardValues.EMPTY, -1, -1)
        self.add_tile(NumberedRoomTileValues.EIGHT, -1, 0)
        self.add_tile(DungeonCardValues.EMPTY, -1, 1)
        self.add_tile(DungeonCardValues.EMPTY, -1, 2)
        self.add_tile(NumberedRoomTileValues.TWELVE, 0, -3)
        self.add_tile(DungeonCardValues.EMPTY, 0, -2)
        self.add_tile(NumberedRoomTileValues.SEVEN, 0, -1)
        self.add_tile(NumberedRoomTileValues.NINE, 0, 0)
        self.add_tile(NumberedRoomTileValues.ONE, 0, 1)
        self.add_tile(NumberedRoomTileValues.TWO, 0, 2)
        self.add_tile(DungeonCardValues.EMPTY, 1, -4)
        self.add_tile(DungeonCardValues.EMPTY, 1, -3)
        self.add_tile(DungeonCardValues.EMPTY, 1, -2)
        self.add_tile(NumberedRoomTileValues.THREE, 1, 0)
        self.add_tile(DungeonCardValues.EMPTY, 1, 1)
        self.add_tile(DungeonCardValues.EMPTY, 1, 2)
        self.add_tile(NumberedRoomTileValues.FIVE, 2, -5)
        self.add_tile(NumberedRoomTileValues.FOUR, 2, -4)
        self.add_tile(DungeonCardValues.EMPTY, 2, -3)
        self.add_tile(DungeonCardValues.EMPTY, 2, 0)
        self.add_tile(DungeonCardValues.EMPTY, 2, 1)
        self.add_tile(DungeonCardValues.EMPTY, 2, 2)
        self.add_tile(UniqueDungeonCardValues.EXIT_A, 3, -6)
        self.add_tile(NumberedRoomTileValues.SIX, 3, -5)
        self.add_tile(DungeonCardValues.EMPTY, 3, -4)
        self.add_tile(DungeonCardValues.EMPTY, 3, 0)
        self.add_tile(UniqueDungeonCardValues.ENTRANCE_A, 3, 1)
