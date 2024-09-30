from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    product = 1
    num_zerosIxs = []
    for i, num in enumerate(nums):
        product *= num
        if num == 0:
            num_zerosIxs.append(i)
    
    if num_zerosIxs == []:
        return [product // i for i in nums]

    elif len(num_zerosIxs) == 1:
        result = [0] * len(nums)
        zeroIx = 0
        product = 1
        for i, num in enumerate(nums):
            if num != 0:
                product *= num
            else:
                zeroIx = i
        result[zeroIx] = product
        return result

    else:
        return [0] * len(nums)
    

print(productExceptSelf([1,2,3,4]), [24,12,8,6])
print(productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])