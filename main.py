#!/usr/bin/env python3
import tcod
from engine import Engine
from game_map import GameMap
from input_handlers import EventHandler
from entity import Entity

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 0, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 255))
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)

    My_engine = Engine(entities, event_handler, game_map, player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Sprinkles Future Triggering Adventure",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            My_engine.render(root_console, context)
            
            events = tcod.event.wait()

            My_engine.handle_events(events)

if __name__ == "__main__":
    main()