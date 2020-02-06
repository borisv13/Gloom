from backend.src.main.game.values import UniqueDungeonCardValues
from backend.src.main.room.waypoint.waypoint_pojo import WaypointPOJO


class WaypointA(WaypointPOJO):
    def __init__(self):
        super(WaypointA, self).__init__(
            UniqueDungeonCardValues.ENTRANCE_A,
            UniqueDungeonCardValues.EXIT_A
        )
