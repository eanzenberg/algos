from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
    S.sort()
    if S[-1] % 3 == 0:
        return S[-1] // 3 + int(any(x % 3 != 0 for x in S))
    if S[-1] % 3 == 1 and 1 not in S and S[-1] - 1 not in S:
        return S[-1] // 3 + 1
    num_threes = S[-1] // 3
    num_twos = 0
    num_ones = 0
    mod1, mod2 = False, False
    for num in S:
        if num % 3 == 1:
            mod1 = True
        if num % 3 == 2:
            mod2 = True
        if mod1 and mod2:
            num_ones = 2
            break

    if mod1 and not mod2:
        num_ones = 1
    if mod2 and not mod1:
        num_twos = 1
    print([1] * num_ones + [2] * num_twos + [3] * num_threes)
    return num_ones + num_twos + num_threes


print(getMinProblemCount(6, [1, 2, 3, 4, 5, 6]), 3) # [1, 2, 3]
print(getMinProblemCount(5, [1, 2, 3, 4, 5]), 3)
print(getMinProblemCount(4, [4, 3, 3, 4]), 2)
print(getMinProblemCount(4, [2, 4, 6, 8]), 4)
print(getMinProblemCount(7, [2, 4, 6, 8, 10, 12, 14]), 6)
print(getMinProblemCount(6, [1, 2, 3, 5, 7, 8]), 4)
print(getMinProblemCount(1, [8]), 3)
print(getMinProblemCount(3, [2, 4, 6]), 3) # [1, 2, 3]
print(getMinProblemCount(3, [2, 4, 7]), 3) # [2, 2, 3]
print(getMinProblemCount(4, [2, 4, 6, 7]), 4) # [1, 2, 2, 3]
print(getMinProblemCount(5, [2, 3, 5, 8, 10]), 4) # [2, 2, 3, 3] [1, 1, 3, 3, 3]
