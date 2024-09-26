from typing import List
from collections import defaultdict


def permuteUnique(nums: List[int]) -> List[List[int]]:
    def permute(nums: List[int]) -> List[List[int]]:
        permutations = defaultdict(list)        
        
        if len(nums) == 1:
            permutations[tuple(nums)] = None
            return permutations
        
        for i in range(len(nums)):
            item = nums[i]
            remaining_list = nums[:i] + nums[i+1:]

            for remaining_items in permute(remaining_list):
                key = [item] + list(remaining_items)
                if tuple(key) not in permutations:
                    permutations[tuple(key)] = None

        return permutations

    return [list(i) for i in permute(nums).keys()]


print(permuteUnique([1,2,3]), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
print(permuteUnique([1,1,2]), [[1,1,2],[1,2,1],[2,1,1]])
print(permuteUnique([1]), [[1]])