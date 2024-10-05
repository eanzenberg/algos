from typing import List
from collections import defaultdict

def longestPath(parent: List[int], s: str) -> int:
    graph = defaultdict(list)
    for i, node in enumerate(parent):
        graph[node].append(i)

    print(graph)

    result = 0

    def dfs(node):
        nonlocal result

        longest = second_longest = 0

        for child in graph[node]:
            length = dfs(child)

            if s[child] != s[node]:
                if length > longest:
                    second_longest = longest
                    longest = length
                elif length > second_longest:
                    second_longest = length
            print(child, node, length, longest, second_longest, result)

        if longest + second_longest + 1 > result:
            result = longest + second_longest + 1
        return longest + 1

    dfs(0)
    return result


print(longestPath([-1,0,0,1,1,2], "abacbe"), 3)
print(longestPath([-1,0,0,0], "aabc"), 3)