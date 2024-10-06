from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    indices = list()
    sums = list()
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if i < j:
                indices.append((i, j))
                sums.append(nums[i] + nums[j])
    
    print(indices, sums)

    result_indices = set()

    for i, sum_i in enumerate(sums):
        for j, sum_j in enumerate(sums):
            if i < j and sum_i + sum_j == target and not any(x in indices[i] for x in indices[j]):
                sorted_indices = sorted(indices[i] + indices[j])
                result_indices.add(tuple(sorted_indices))
 
    result = set()
    for result_indices in result_indices:
        result.add(tuple(sorted(nums[x] for x in result_indices)))

    return [list(x) for x in result]


print(fourSum([1,0,-1,0,-2,2], 0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
print(fourSum([2,2,2,2,2], 8), [[2,2,2,2]])