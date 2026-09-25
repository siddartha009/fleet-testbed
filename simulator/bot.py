class Bot:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.path = []

    def set_path(self, path):
        self.path = list(path)

    def move(self):
        """Move one step along the path. Does nothing if path is empty."""
        if self.path:
            self.x, self.y = self.path.pop(0)

    def has_arrived(self):
        return len(self.path) == 0