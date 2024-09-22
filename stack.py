from typing import List


def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    count = 0
    for i in reversed(range(1, N)):
        if R[i] <= i:
            return -1
        if R[i-1] >= R[i]:
            R[i-1] = R[i] - 1
            count += 1
    return count


print(getMinimumDeflatedDiscCount(5, [2, 5, 3, 6, 5]), 3)
print(getMinimumDeflatedDiscCount(3, [100, 100, 100]), 2)
print(getMinimumDeflatedDiscCount(4, [6, 5, 4, 3]), -1)
print(getMinimumDeflatedDiscCount(1, [1]), 0)