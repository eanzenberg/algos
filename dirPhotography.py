from typing import List


def findAllCharsWithinDistance(str, X, Y, char, locRoot, direction = 'lr') -> List:
    res = []

    # Right
    if 'r' in direction:
        start = min(locRoot + X, len(str))
        end = min(len(str), locRoot + Y + 1)
        found = [i for i, x in enumerate(str[start: end], start = start) if x == char]
        res.extend(found)

    # Left
    if 'l' in direction:
        start = max(0, locRoot - Y)
        end = max(locRoot - X + 1, 0)
        found = [i for i, x in enumerate(str[start: end], start = start) if x == char]
        res.extend(found)
    return res


def _getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    count = 0
#    print([(i, x) for i, x in enumerate(C)])
    for i, cell in enumerate(C):
        if cell == 'P' and 'A' in C[max(0, i - Y): min(N, i + Y + 1)] and 'B' in C[max(0, i - 2*Y): min(N, i + 2*Y + 1)]:
            for direction in 'lr':
                foundA = findAllCharsWithinDistance(C, X, Y, 'A', i, direction)
                for A in foundA:
                    foundB = findAllCharsWithinDistance(C, X, Y, 'B', A, direction)
#                    print(direction, i, A, foundB)
                    count += len(foundB)
    return count


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    count = 0
    prefixP = [0]
    prefixB = [0]
#    print([(i, x) for i, x in enumerate(C)])
    for c in C:
        if c == 'P':
            prefixP.append(prefixP[-1] + 1)
        else:
            prefixP.append(prefixP[-1])
        if c == 'B':
            prefixB.append(prefixB[-1] + 1)
        else:
            prefixB.append(prefixB[-1])

    for i, c in enumerate(C):
        if c == 'A':
            # (P <- A <- B)
            startL = max(0, i - Y)
            endL = max(0, i - X + 1)
            startR = min(N, i + X)
            endR = min(N, i + Y + 1)
            countP = prefixP[endL] - prefixP[startL]
            countB = prefixB[endR] - prefixB[startR]
            count += countB * countP
            #print('l', i, countP, countB)

            # (B -> A -> P)
            countB = prefixB[endL] - prefixB[startL]
            countP = prefixP[endR] - prefixP[startR]
            count += countB * countP
            #print('r', i, countP, countB)

    return count



print('1: ', getArtisticPhotographCount(5, "APABA", 1, 1), 1)
print('2: ', getArtisticPhotographCount(10, "APABA....B", 1, 5), 2)
print('3: ', getArtisticPhotographCount(10, "APABA....B"[::-1], 1, 5), 2)
print('2: ', getArtisticPhotographCount(5, "APABA", 2, 3), 0)
print('3: ', getArtisticPhotographCount(8, ".PBAAP.B", 1, 3), 3)