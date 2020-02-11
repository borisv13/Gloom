# pylint: disable=line-too-long
from unittest.mock import call, patch

import pytest
from backend.src.main.game.dungeon.random_dungeon_generator import RandomDungeonGenerator
from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.room.abstract_room_card import AbstractRoomCard
from backend.src.main.game.room.constructed_room import ConstructedRoom
from backend.src.main.game.room.waypoint.waypoint_a import WaypointA
from backend.src.main.game.tile.tile_geometry import TileGeometry
from backend.src.main.wrappers.random_wrapper import RandomWrapper
from backend.src.test.game.dungeon import util


def test_dungeon_generator_has_20_monster_cards(dungeon_generator):
    assert len(dungeon_generator.monster_cards) == 20
    for item in dungeon_generator.monster_cards:
        assert isinstance(item, AbstractMonsterCard)


def test_dungeon_generator_has_20_room_cards(dungeon_generator):
    assert len(dungeon_generator.room_cards) == 20
    for item in dungeon_generator.room_cards:
        assert isinstance(item, AbstractRoomCard)


def test_dungeon_is_composed_of_twenty_distinct_room_cards(dungeon_generator):
    assert len(dungeon_generator.room_cards) == 20
    room_card_names = {room.name for room in dungeon_generator.room_cards}
    assert len(room_card_names) == 20


def test_dungeon_is_composed_of_twenty_distinct_monster_cards(dungeon_generator):
    assert len(dungeon_generator.monster_cards) == 20
    dungeon_card_names = {monster.name for monster in dungeon_generator.monster_cards}
    assert len(dungeon_card_names) == 20


def test_dungeon_generator_has_no_rooms_initially(dungeon_generator):
    assert not dungeon_generator.constructed_rooms


def test_select_first_room_reduces_deck_sizes_by_one(dungeon_generator):
    dungeon_generator.select_first_room()
    assert len(dungeon_generator.room_cards) == 19
    assert len(dungeon_generator.monster_cards) == 19


def test_select_first_room_adds_constructed_room(dungeon_generator):
    dungeon_generator.select_first_room()
    assert len(dungeon_generator.constructed_rooms) == 1
    assert isinstance(dungeon_generator.constructed_rooms[0], ConstructedRoom)


def test_select_first_room_calls_random_choice_twice(dungeon_generator):
    expected_room_argument = 20
    expected_monster_argument = 20
    expected_calls = [call(expected_room_argument), call(expected_monster_argument)]

    with patch.object(RandomWrapper, 'randrange', side_effect=[0, 0]) as mock:
        dungeon_generator.select_first_room()

        mock.assert_has_calls(expected_calls)
        assert mock.call_count == 2


def test_select_room_waypoint_a_checks_if_drawn_card_has_entrance_a(dungeon_generator, waypoint_a):
    room_with_exit = util.get_room_with_exit_a(dungeon_generator)

    for room in dungeon_generator.room_cards:
        if waypoint_a.has_entrance(room) and room != room_with_exit:
            room_with_entrance = room

    with patch.object(RandomDungeonGenerator, 'select_room_card', side_effect=[room_with_exit, room_with_entrance]):
        dungeon_generator.select_first_room()

    assert len(dungeon_generator.constructed_rooms) == 1
    with patch.object(WaypointA, 'has_entrance', wraps=waypoint_a.get_entrance) as mock:
        dungeon_generator.select_room_by_waypoint(waypoint_a)
        assert mock.call_count >= 1


def test_select_room_waypoint_raises_value_error_if_does_not_have_exit(dungeon_generator, waypoint_a):
    for room in dungeon_generator.room_cards:
        if not waypoint_a.has_exit(room):
            room_with_no_exit = room

    for room in dungeon_generator.room_cards:
        if room != room_with_no_exit:
            room_with_entrance = room

    with patch.object(RandomDungeonGenerator, 'select_room_card', side_effect=[room_with_no_exit, room_with_entrance]):
        dungeon_generator.select_first_room()
        assert len(dungeon_generator.constructed_rooms) == 1
    with pytest.raises(ValueError, match="Cannot use provided waypoint as room does not have corresponding exit."):
        dungeon_generator.select_room_by_waypoint(waypoint_a)


def test_select_room_by_waypoint_calls_overlay_room(dungeon_generator, waypoint_a):
    room_with_exit = util.get_room_with_exit_a(dungeon_generator)
    with patch.object(RandomDungeonGenerator, 'select_room_card', return_value=room_with_exit):
        dungeon_generator.select_first_room()
    assert len(dungeon_generator.constructed_rooms) == 1

    with patch.object(TileGeometry, 'overlay_room_a_on_room_b', wraps=TileGeometry.overlay_room_a_on_room_b) as mock:
        dungeon_generator.select_room_by_waypoint(waypoint_a)
        assert mock.call_count == 1


def test_select_room_by_waypoint_causes_two_constructed_rooms_to_be_in_list(dungeon_generator, waypoint_a):
    room_with_exit_a = util.get_room_with_exit_a(dungeon_generator)

    with patch.object(RandomDungeonGenerator, 'select_room_card', return_value=room_with_exit_a):
        dungeon_generator.select_first_room()

    dungeon_generator.select_room_by_waypoint(waypoint_a)
    assert len(dungeon_generator.constructed_rooms) == 2


def test_select_room_by_waypoint_causes_monster_cards_to_be_length_18(dungeon_generator, waypoint_a):
    room_with_exit_a = util.get_room_with_exit_a(dungeon_generator)
    with patch.object(RandomDungeonGenerator, 'select_room_card', return_value=room_with_exit_a):
        dungeon_generator.select_first_room()
    assert len(dungeon_generator.room_cards) == 19
    assert len(dungeon_generator.monster_cards) == 19
    dungeon_generator.select_room_by_waypoint(waypoint_a)
    assert len(dungeon_generator.room_cards) == 18
    assert len(dungeon_generator.monster_cards) == 18


def test_select_room_is_called_twice_when_first_room_chosen_does_not_have_a_valid_entrance(dungeon_generator,
                                                                                           waypoint_a):
    room_one = util.get_room_with_exit_a(dungeon_generator)

    with patch.object(RandomDungeonGenerator, 'select_room_card', return_value=room_one) as mock:
        dungeon_generator.select_first_room()
        assert mock.call_count == 1

    select_room_return_values = []

    for room in dungeon_generator.room_cards:
        if not waypoint_a.has_entrance(room) and room not in select_room_return_values:
            select_room_return_values.append(room)
            break
    assert len(select_room_return_values) == 1

    for room in dungeon_generator.room_cards:
        if waypoint_a.has_entrance(room) and room not in select_room_return_values:
            select_room_return_values.append(room)
            break
    assert len(select_room_return_values) == 2

    with patch.object(RandomDungeonGenerator, 'select_room_card', side_effect=select_room_return_values) as mock:
        dungeon_generator.select_room_by_waypoint(waypoint_a)
        assert mock.call_count == 2
