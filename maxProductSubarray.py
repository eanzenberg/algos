from typing import List


def maxProduct(nums: List[int]):
    def prod_of_array(nums: List[int]):
        if nums == []:
            return -float("inf")
        product = 1
        for num in nums:
            product *= num
        return product
    
    if len(nums) == 1:
        return nums[0]
    
    sub_arrays_to_try = []
    sub_zero = []
    has_zero = False
    for num in nums:
        if num < 0 or num > 0:
            sub_zero.append(num)
        else:
            has_zero = True
            if sub_zero:
                sub_arrays_to_try.append(sub_zero)
            sub_zero = []

    if has_zero:
        sub_arrays_to_try.append([0])

    if sub_zero:
        sub_arrays_to_try.append(sub_zero)

    if not sub_arrays_to_try:
        return 0
    
    print(nums, sub_arrays_to_try)

    max_product = -float("inf")
    for array_to_try in sub_arrays_to_try:
        if len(array_to_try) == 1:
            if array_to_try[0] > max_product:
                max_product = array_to_try[0]
        else:
            tmp_prod = prod_of_array(array_to_try)
            if tmp_prod > 0 and tmp_prod > max_product:
                max_product = tmp_prod
            elif tmp_prod < 0:
                first_neg = last_neg = -1
                for i in range(len(array_to_try)):
                    if array_to_try[i] < 0 and first_neg == -1:
                        first_neg = i
                    if array_to_try[::-1][i] < 0 and last_neg == -1:
                        last_neg = len(array_to_try) - i - 1
                    if first_neg != -1 and last_neg != -1:
                        break
                print("first, last: ", first_neg, last_neg)
                if first_neg == last_neg:
                    first_array = array_to_try[0: first_neg]
                    second_array = array_to_try[first_neg + 1:] if first_neg + 1 < len(array_to_try) else []
                    tmp_prod = max(prod_of_array(first_array), prod_of_array(second_array))
                    if tmp_prod > max_product:
                        max_product = tmp_prod
                else:
                    first_array = array_to_try[first_neg + 1:]
                    second_array = array_to_try[:last_neg]
                    tmp_prod = max(prod_of_array(first_array), prod_of_array(second_array))
                    if tmp_prod > max_product:
                        max_product = tmp_prod

    return max_product


print(maxProduct([2,-5,-2,-4,3]), 24)
print(maxProduct([-3,0,1,-2]), 1)
print(maxProduct([2,3,-2,4,-1, 1, -1, 1, -1, 1]), 48)
print(maxProduct([2,3,-2,4,0, -1, 1, 1, -1, -1, 1]), 6)
print(maxProduct([-2,3,-2,4,0, -1, 1, 1, 1, -1, 1]), 48)
print(maxProduct([2,3,-2,4]), 6)
print(maxProduct([-2,0,-1]), 0)
print(maxProduct([-3,-1,-1]), 3)
print(maxProduct([0,2]), 2)
print(maxProduct([0]), 0)
print(maxProduct([3]), 3)
print(maxProduct([0, 0]), 0)
print(maxProduct([2, 0, 1, 0, -5]), 2)