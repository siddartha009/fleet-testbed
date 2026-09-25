from grid import Grid
from bot import Bot
from pathfinder import find_path

GRID_WIDTH = 10
GRID_HEIGHT = 10
START = (0, 0)
TARGET = (6, 4)
WALL = [(3, 0), (3, 1), (3, 2), (3, 3)]  # a vertical wall segment

grid = Grid(GRID_WIDTH, GRID_HEIGHT)
for cell in WALL:
    grid.add_obstacle(*cell)

path = find_path(grid, START, TARGET)
if not path:
    print("No path found!")
else:
    bot = Bot(START[0], START[1])
    bot.set_path(path)

    last_direction = None
    while not bot.has_arrived():
        prev_x, prev_y = bot.x, bot.y
        bot.move()
        direction = (bot.x - prev_x, bot.y - prev_y)
        note = " (routing around obstacle)" if last_direction and direction != last_direction else ""
        print((bot.x, bot.y), note)
        last_direction = direction