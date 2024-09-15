from typing import List


def _getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    seats = [x - 1 for x in sorted(S)]
    occupied = [False] * N
    for seat in seats:
        start = max(0, seat - K)
        end = min(N, seat + K + 1)
        for i in range(start, end):
            occupied[i] = True
    additional_diners = 0
    print([(i + 1, x) for i, x in enumerate(occupied)])
    i = 0
    while i < N:
        if not occupied[i]:
            additional_diners += 1
            print("additional diners: ", i)
            i += K
        i += 1

    return additional_diners


def ceil_div(a, b):
    return -(a // -b)


def getMaxAdditionalDinersCount(N, K, M, S):
    if M == 0:
        return ceil_div(N, K + 1)

    S.sort()
    # Left side
    _to_add = ceil_div(S[0] - K - 1, K + 1) if (S[0] - K - 1) > 0 else 0
    additional_diners = _to_add
    print("left: ", _to_add)

    # Right side
    _to_add = ceil_div(N - S[-1] - K, K + 1) if (N - S[-1] - K) > 0 else 0
    additional_diners += _to_add
    print("right: ", _to_add)

    # Middle
    if M > 1:
        for i in range(1, len(S)):
            _to_add = ceil_div(S[i] - S[i - 1] - 2 * K - 1, K + 1)
            additional_diners += _to_add
            print(f"middle: {S[i]}, added: {_to_add}")

    return additional_diners


print(_getMaxAdditionalDinersCount(10, 1, 2, [6, 4]), 3)
print(getMaxAdditionalDinersCount(10, 1, 2, [6, 4]), 3)
print(_getMaxAdditionalDinersCount(10, 1, 0, []), 5)
print(getMaxAdditionalDinersCount(10, 1, 0, []), 5)
print(_getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 14]), 1)
print(getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 14]), 1)
print(getMaxAdditionalDinersCount(10000000, 1000, 0, []), 9991)
print(_getMaxAdditionalDinersCount(1000, 1, 0, []), 9990)
print(getMaxAdditionalDinersCount(1000, 1, 0, []), 500)
print(getMaxAdditionalDinersCount(100, 1, 50, [i for i in range(1, 101) if i % 2 == 1]), 0)
print(getMaxAdditionalDinersCount(10, 0, 2, [2, 6]), 8)
print(getMaxAdditionalDinersCount(1000, 3, 3, [100, 500, 900]), 247)
print(getMaxAdditionalDinersCount(20, 2, 2, [1, 20]), 5)
print(getMaxAdditionalDinersCount(20, 2, 1, [10]), 6)
print(getMaxAdditionalDinersCount(50, 5, 1, [25]), 8)
print(getMaxAdditionalDinersCount(10, 20, 1, [1]), 0)
