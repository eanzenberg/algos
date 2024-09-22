from typing import List


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    lookback = {}
    count = 0
    for d in D:
        if not d in lookback or (count - lookback[d]) > K:
            lookback[d] = count
            count += 1
    return count


print(getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 1), 5)
print(getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 2), 4)
print(getMaximumEatenDishCount(7, [1, 2, 1, 2, 1, 2, 1], 2), 2)