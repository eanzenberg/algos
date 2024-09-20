from typing import List
from functools import cmp_to_key

def largestNumber(nums: List[int]) -> str:
    def compare(item1, item2):
        return -1 if str(item1) + str(item2) > str(item2) + str(item1) else 1

    sorted_nums = sorted(nums, key = cmp_to_key(compare))
    print(sorted_nums)
    return "".join(map(str, sorted_nums)) if sorted_nums[0] != 0 else "0"

print(largestNumber([3,30,34,5,9]))
print(largestNumber([1, 5, 4, 3, 2, 1]))
print(largestNumber([10, 2]))
print(largestNumber([0, 0]))
