from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
    S.sort()
    num_twos = S[-1] // 2
    num_ones = 0
    for num in S:
        if num % 2 == 1:
            num_ones = 1
            break
    return num_ones + num_twos


print(getMinProblemCount(6, [1, 2, 3, 4, 5, 6]), 4)
print(getMinProblemCount(4, [4, 3, 3, 4]), 3)
print(getMinProblemCount(4, [2, 4, 6, 8]), 4)
print(getMinProblemCount(6, [1, 2, 3, 5, 7, 8]), 5)
[1, 2, 2, 2, 1]
