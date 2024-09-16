from typing import List
import sys
sys.setrecursionlimit(10**6)

def _getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    reached = dict()
    res = 0
    for i, l in enumerate(L):
        reached[i+1] = []
        ii = l
        first = True
        while ii not in reached[i+1]:
            if first:
                reached[i+1].append(i+1)
                first = False
            if ii in reached and L[ii - 1] not in reached:
                _to_extend = reached[ii]
                reached[i+1].extend(_to_extend)
                break
            reached[i+1].append(ii)
            ii = L[ii - 1]
        length = len(reached[i+1])
        if length > res:
            res = length
    print(reached)
    return res

def longest_unique_path(graph):
    def dfs(node, visited):
        visited.add(node)
        max_length = 1  # At least the current node
        path = [node]  # Start the path with the current node

        # Explore all possible paths
        if node in graph and graph[node] not in visited:
            next_length, next_path = dfs(graph[node], visited.copy())
            max_length += next_length
            path += next_path

        return max_length, path

    max_path_len = 0
    longest_path = []

    # Try starting from each node
    for start_node in graph:
        length, path = dfs(start_node, set())
        if length > max_path_len:
            max_path_len = length
            longest_path = path

    return longest_path, max_path_len


def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    visited_graph = {}
    def traverse(x):
        if x in visited_graph.keys():
            return
        else:
            visited_graph[x] = L[x - 1]
            traverse(L[x - 1])

    for i in range(1, N+1):
        traverse(i)
    print(f"{visited_graph}")

    result = longest_unique_path(visited_graph)
    print(result)
    return result[1]


print(getMaxVisitableWebpages(4, [4, 1, 2, 1]), 4)
print(getMaxVisitableWebpages(5, [4, 3, 5, 1, 2]), 3)
print(getMaxVisitableWebpages(5, [2, 4, 2, 2, 3]), 4)