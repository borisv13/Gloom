from backend.src.main.game.monster.random_monster_card import RandomMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues, \
    TrapIndicators


class Horrific(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWO: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.EMPTY,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN:
                          [DungeonCardValues.TRAPS, TrapIndicators.MUDDLE, TrapIndicators.DAMAGE],
                      NumberedRoomTileValues.EIGHT: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.NINE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TEN:
                          [DungeonCardValues.TRAPS, TrapIndicators.MUDDLE, TrapIndicators.DAMAGE],
                      NumberedRoomTileValues.ELEVEN:
                          [DungeonCardValues.TRAPS, TrapIndicators.MUDDLE, TrapIndicators.DAMAGE],
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER}
        RandomMonsterCard.__init__(self, "Horrific", map_values)
