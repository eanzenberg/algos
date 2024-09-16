from typing import List


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    total = 0
    low, high = C[0] - 1, C[0] - 1 + N
    total += min(abs(N - low), abs(N - high))
    print(f"{low}, {high}, {total}")
    for i in range(1, M):
        low, high = C[i - 1] - 1, C[i - 1] - 1 + N
        num = C[i] - 1 if low <= C[i] - 1 <= high else C[i] - 1 + N
        total += min(abs(num - low), abs(num - high))
        print(f"{low}, {high}, {num}, {total}")
    return total

print(getMinCodeEntryTime(3, 3, [1, 2, 3]), 2)
print(getMinCodeEntryTime(10, 4, [9, 4, 4, 8]), 11)
