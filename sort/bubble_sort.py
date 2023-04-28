from typing import List


def bubble_sort(nums: List[int]) -> None:
    n = len(nums)
    while n > 1:
        for left in range(n-1):
            if nums[left] > nums[left+1]:
                nums[left], nums[left+1] = nums[left+1], nums[left]
        n -= 1
    return 


