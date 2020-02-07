from backend.src.main.game.random_monster_card import RandomMonsterCard
from backend.src.main.game.values import DungeonCardValues, NumberedRoomTileValues


class Putrid(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):

        map_values = {
            NumberedRoomTileValues.TWO: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.FIVE: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.EIGHT: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.NINE: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE
        }
        RandomMonsterCard.__init__(self, "Putrid", map_values)