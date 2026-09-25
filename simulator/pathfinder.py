from collections import deque
def find_path(grid, start, target):
    queue = deque([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()
        if current == target:
            break
        x, y = current
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = (x + dx, y + dy)
            if neighbor not in came_from and grid.is_free(*neighbor):
                came_from[neighbor] = current
                queue.append(neighbor)

    if target not in came_from:
        return []

    path = []
    step = target
    while step != start:
        path.append(step)
        step = came_from[step]
    path.reverse()
    return path