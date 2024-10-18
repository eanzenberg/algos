import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    heapq.heapify([x for x in nums])
    print(nums, heapq.nlargest(k, nums)[-1])
    return heapq.nlargest(k, nums)[-1]


print(findKthLargest([3,2,1,5,6,4], 2), 5)
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)