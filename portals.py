from typing import List
from collections import deque, defaultdict


def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    map_of_field = {}
    inv_map_of_field = defaultdict(list)
    for x in range(R):
        for y in range(C):
            map_of_field[x, y] = G[x][y]
            inv_map_of_field[G[x][y]].append((x, y))

    startX, startY = inv_map_of_field['S'][0]

    queue = deque([(startX, startY, 0)])

    print(map_of_field, '\n', inv_map_of_field)

    visited = {}
    found_end = []
    while queue:
        x, y, length = queue.popleft()
        if (x, y) in visited or map_of_field[x, y] == '#':
            continue

        if map_of_field[x, y] == 'E':
            found_end.append(length)

        if map_of_field[x, y].isalpha() and map_of_field[x, y] not in 'SE':
            other_portals = inv_map_of_field[map_of_field[x, y]]
            other_portals.remove((x, y))
            for other_portal in other_portals:
                queue.append((other_portal[0], other_portal[1], length + 1))

        visited[x, y] = None
        if y < C - 1:
            queue.append((x, y + 1, length + 1))
        if y > 0:
            queue.append((x, y - 1, length + 1))
        if x > 0:
            queue.append((x - 1, y, length + 1))
        if x < R - 1:
            queue.append((x + 1, y, length + 1))

    if not found_end:
        return -1
    else:
        return min(found_end)


print(getSecondsRequired(3, 3, [".E.", ".#E", ".S#"]), 4)
print(getSecondsRequired(3, 4, ["aS.b", "####", "Eb.a"]), 4)
