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


def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    visited_graph = {}
    def directed_graph(x):
        if x in visited_graph.keys():
            return
        else:
            visited_graph[x] = L[x - 1]
            directed_graph(L[x - 1])

    for i in range(1, N+1):
        directed_graph(i)

 #   print(f"{visited_graph}")

    loops = {}
    chain = {}

    def traverse(k, length, visited_in_loop):
        v = visited_graph[k]
#        print(f"traverse: {k}, {v}, {chain}, {visited_in_loop}")
        if k in loops.keys():
            pass
        elif k == v:
            chain[v] = 1
        elif v in loops.keys():
            visited_in_loop.append(k)
            loop_length = loops[v]
            for i, kk in enumerate(visited_in_loop[::-1]):
                chain[kk] = loop_length + i + 1
        elif v in chain and visited_graph[v] != k and v not in visited_in_loop:
            chain[k] = chain[v] + 1
        elif v in chain and v in visited_in_loop:
            visited_in_loop.append(k)
            ix = visited_in_loop.index(v)
            loop_length = len(visited_in_loop) - ix
            loops[k] = loop_length
            chain[k] = loop_length
            for i, kk in enumerate(visited_in_loop[0:ix][::-1]):
                chain[kk] = loop_length + i + 1
            for kk in visited_in_loop[ix:]:
                loops[kk] = loop_length
                chain[kk] = loop_length
        while k not in chain:
            length += 1
            chain[k] = length
            visited_in_loop.append(k)
            traverse(v, length, visited_in_loop)

    for k, v in visited_graph.items():
        length = 0
        traverse(k, length, [])
#        print(k, v, chain, loops)
#    print(chain, loops)
    return max(chain.values())


print(getMaxVisitableWebpages(4, [4, 1, 2, 1]), 4)
print(getMaxVisitableWebpages(5, [4, 3, 5, 1, 2]), 3)
print(getMaxVisitableWebpages(6, [4, 3, 5, 1, 2, 2]), 4)
print(getMaxVisitableWebpages(5, [2, 4, 2, 2, 3]), 4)
print(getMaxVisitableWebpages(8, [2, 4, 2, 2, 3, 4, 6, 7]), 5)
print(getMaxVisitableWebpages(5, [2, 3, 4, 5, 1]), 5)
print(getMaxVisitableWebpages(6, [2, 1, 4, 3, 6, 5]), 2)
print(getMaxVisitableWebpages(5, [2, 3, 4, 5, 3]), 5)
print(getMaxVisitableWebpages(5, [2, 3, 4, 5, 4]), 5)
print(getMaxVisitableWebpages(6, [2, 3, 4, 2, 6, 5]), 4)
print(getMaxVisitableWebpages(2, [1, 2]), 2)
print(getMaxVisitableWebpages(7, [2, 3, 4, 5, 1, 7, 5]), 7)
print(getMaxVisitableWebpages(8, [2, 3, 4, 5, 1, 7, 8, 5]), 8)
print(getMaxVisitableWebpages(5, [1, 2, 3, 4, 5]), 1)
print(getMaxVisitableWebpages(500000, list(range(2, 500001)) + [1]), 500000)
print(getMaxVisitableWebpages(500000, [i + 1 if i % 2 == 1 else i - 1 for i in range(1, 500001)]), 2)
print(getMaxVisitableWebpages(499999, list(range(2, 500000)) + [1]), 499999)
