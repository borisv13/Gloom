from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues


class Fortified(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWO: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.THREE: DungeonCardValues.COIN,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.COIN,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.EIGHT: DungeonCardValues.TRAPS,
                      NumberedRoomTileValues.NINE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TEN: DungeonCardValues.TRAPS,
                      NumberedRoomTileValues.ELEVEN: DungeonCardValues.TRAPS,
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.MONSTER}
        AbstractMonsterCard.__init__(self, "Fortified", map_values)
