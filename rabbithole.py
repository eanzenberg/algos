from typing import List

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
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
            reached[i+1].append(ii)
            ii = L[ii - 1]
        length = len(set(reached[i+1]))
        if length > res:
            res = length
    print(reached)
    return res


print(getMaxVisitableWebpages(4, [4, 1, 2, 1]), 4)
print(getMaxVisitableWebpages(5, [4, 3, 5, 1, 2]), 3)
print(getMaxVisitableWebpages(5, [2, 4, 2, 2, 3]), 4)