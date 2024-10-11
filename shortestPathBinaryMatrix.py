from collections import deque
from typing import List


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    max_length = len(grid[0])
    queue = deque([(0, 0, 1)])
    visited = set()
    visited.add((0, 0))

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    if grid[0][0] == 1 or grid[max_length - 1][max_length - 1] == 1:
        return -1

    while queue:
        x, y, length = queue.popleft()

        if x == max_length - 1 and y == max_length - 1:
            return length

        for dx, dy in directions:
            new_x, new_y  = x + dx, y + dy
            if ((0 <= new_x < max_length) and 
                (0 <= new_y < max_length) and 
                ((new_x, new_y) not in visited) and
                (grid[new_y][new_x] == 0)):

                queue.append((new_x, new_y, length + 1))
                visited.add((new_x, new_y))
                print(x, y, new_x, new_y, queue, visited)

    return -1


print(shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]), 4)
print(shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]), -1)