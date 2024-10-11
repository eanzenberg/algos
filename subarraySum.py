from typing import List
from collections import defaultdict


def subarraySumPositiveOnly(nums: List[int], k: int) -> int:
    solutions = 0
    local_sum = nums[0]
    start, end = 0, 0
    while start < len(nums):
        if start > end:
            end = start
            local_sum = nums[start]

        if local_sum < k:
            end += 1
            if end == len(nums):
                break
            local_sum += nums[end]

        elif local_sum > k:
            local_sum -= nums[start]
            start += 1

        else:
            solutions += 1
            local_sum -= nums[start]
            start += 1

    return solutions


def subarraySum(nums: List[int], k: int) -> int:
    prefix_sums = defaultdict(int)

    local_sum = 0
    solutions = 0

    for num in nums:
        local_sum += num
        if local_sum == k:
            solutions += 1

        if (local_sum - k) in prefix_sums:
            solutions += prefix_sums[local_sum - k]

        prefix_sums[local_sum] += 1
        print(num, prefix_sums, local_sum, k, solutions)
    return solutions


print(subarraySum([1,1,1], 2), 2)
print(subarraySum([1,2,3], 3), 2)
print(subarraySum([1,-1,1,1,1,3], 3), 3)
print(subarraySum([-6,1,-1,1,1,1,3], 0), 3)