from typing import List

def bs_list(haystack: List[int], needle: int) -> bool:
    left = 0
    right = len(haystack)
    while left < right:
        mid = left + (right - left) // 2
        if haystack[mid] == needle:
            return True
        elif haystack[mid] < needle:
            left = mid + 1
        else:
            right = mid
    return False
