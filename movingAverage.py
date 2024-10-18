from collections import deque


def moving_average(nums: list, window_size: int) -> list:
    if not nums:
        return []
    
    if window_size > len(nums):
        return []

    ans = []
    queue = deque(nums[0:window_size])
    running_sum = sum(queue)

    for num in nums[window_size:]:
        ans.append(1. * running_sum / window_size)
        queue.append(num)
        left_num = queue.popleft()
        running_sum += num
        running_sum -= left_num

    ans.append(1. * running_sum / window_size)
    return ans


print(moving_average([1, 2, 3, 4, 5], 1))
print(moving_average([1, 2, 3, 4, 5], 2))
print(moving_average([1, 2, 3, 4, 5], 5))