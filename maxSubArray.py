from typing import List


def maxSubArray(nums: List[int]) -> int:
    sum_before, max_sum = 0, -float("inf")

    for num in nums:
        sum_before = 0 if sum_before < 0 else sum_before
        sum_before += num
        if sum_before > max_sum:
            max_sum = sum_before

    return max_sum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
print(maxSubArray([1]), 1)
print(maxSubArray([5,4,-1,7,8]), 23)
print(maxSubArray([-1]), -1)