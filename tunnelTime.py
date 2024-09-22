from typing import List


def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
    A.sort()
    B.sort()
    L = [y - x for x, y in zip(A, B)]
    prefixL = [L[0]]
    for l in L[1:]:
        prefixL.append(l + prefixL[-1])

    totalL = sum(L)
    print(f"totalL: {totalL}, K: {K}")
    if K % totalL == 0:
        return B[-1] + C * ((K // totalL) - 1)
    tunnelTime = C * (K // totalL)
    leftOver = K % totalL

    print(f"A: {A}\nB: {B}")
    print(f"L: {L}, totalL: {totalL}\npresumL: {prefixL}, tunneltime: {tunnelTime}, leftOver: {leftOver}")

    for i in range(len(prefixL)):
        if leftOver <= prefixL[i]:
            tunnelTime += B[i] - (prefixL[i] - leftOver)
            break

    return tunnelTime


print(getSecondsElapsed(10, 2, [1,6], [3, 7], 7), 22)
print(getSecondsElapsed(10, 2, [1,6], [3, 7], 3), 7)
print(getSecondsElapsed(10, 2, [1,6], [3, 7], 6), 17)
print(getSecondsElapsed(50, 3, [39, 19, 28], [49, 27, 35], 15), 35)
print(getSecondsElapsed(50, 4, [39, 19, 28, 4], [49, 27, 35, 6], 27*2), 99)
print(getSecondsElapsed(10, 1, [1], [2], 1), 2)
print(getSecondsElapsed(10, 2, [1, 6], [3, 8], 50), 123)
print(getSecondsElapsed(10, 2, [1, 4], [3, 8], 6), 8)