from typing import List
import math

def two_crystal_balls(nums: List[bool]) -> int:
    n = len(nums)
    n_sqrt = int(math.sqrt(n))


    not_broken_idx = n_sqrt
    while not_broken_idx < n and not nums[not_broken_idx]:
        not_broken_idx += n_sqrt


    for i in range(not_broken_idx-n_sqrt, n):
        if nums[i]:
            return i
    return -1


