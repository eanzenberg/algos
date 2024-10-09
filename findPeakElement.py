from typing import List

def findPeakElement(nums: List[int]) -> int:
    length = len(nums)
    if length == 1:
        return 0

    start, end = 0, length - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] > nums[mid - 1] and mid + 1 == length:
            return mid

        elif nums[mid] > nums[mid + 1] and mid == 0:
            return mid
        
        elif nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return mid
        
        elif nums[mid + 1] > nums[mid]:
            start = mid + 1
        
        else:
            end = mid - 1

    
print(findPeakElement([1,2,3,1]), 2)
print(findPeakElement([1,2,1,3,5,6,4]), 5)
print(findPeakElement([10,9,8,7,6,5,4]), 0)        
print(findPeakElement([1,2,1,3,5,6,8]), 6)
print(findPeakElement([4, 3, 2, 1, 4]), 6)