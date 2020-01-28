"""Creating Random Monster Card Class:
Archaic
"""
from backend.src.main.game.random_monster_card import RandomMonsterCard
from backend.src.main.game.values import DungeonCardValues, NumberedRoomTileValues


class Archaic(RandomMonsterCard):  # pylint: disable=too-few-public-methods
    """ Class for Archaic Random Monster Card """

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.TWO: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.HAZARDOUS_TERRAIN,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.EIGHT: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.NINE: DungeonCardValues.HAZARDOUS_TERRAIN,
                      NumberedRoomTileValues.TEN: DungeonCardValues.HAZARDOUS_TERRAIN,
                      NumberedRoomTileValues.ELEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE}
        RandomMonsterCard.__init__(self, "Archaic", map_values)