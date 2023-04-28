from typing import List


def linear_search(haystack: List[int], number: int) -> bool:
    for v in haystack:
        if v == number:
            return True
    return False
# TODO: make tests
