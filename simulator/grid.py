MIN_SIZE = 1
MAX_SIZE = 15


class Grid:
    def __init__(self, width, height):
        if not (MIN_SIZE <= width <= MAX_SIZE):
            raise ValueError(f"width must be between {MIN_SIZE} and {MAX_SIZE}, got {width}")
        if not (MIN_SIZE <= height <= MAX_SIZE):
            raise ValueError(f"height must be between {MIN_SIZE} and {MAX_SIZE}, got {height}")

        self.width = width
        self.height = height

    def is_inside(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def add_obstacle(self, x, y):
        """Mark a single cell as blocked."""
        if not hasattr(self, "obstacles"):
            self.obstacles = set()
        self.obstacles.add((x, y))

    def is_blocked(self, x, y):
        return (x, y) in getattr(self, "obstacles", set())

    def is_free(self, x, y):
        return self.is_inside(x, y) and not self.is_blocked(x, y)