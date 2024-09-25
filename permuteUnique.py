from typing import List


def permuteUnique(nums: List[int]) -> List[List[int]]:

    def permute(nums: List[int]):
        if len(nums) == 1:
            return [nums]
        
        permutations = []

        for i in range(len(nums)):
            item = nums[i]
            remaining_list = nums[:i] + nums[i+1:]

            for remaining_items in permute(remaining_list):
                key = [item] + list(remaining_items)
                permutations.append(key)

        return permutations

    return [list(i) for i in set(tuple(i) for i in permute(nums))]
    

print(permuteUnique([1,2,3]), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
print(permuteUnique([1,1,2]), [[1,1,2],[1,2,1],[2,1,1]])