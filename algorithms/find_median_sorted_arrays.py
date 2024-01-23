from typing import List, Optional

class Solution:
    def __init__(self):
        pass

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = nums1
        for num in nums2:
            result.append(num)
        result.sort()
        if len(result) % 2 == 0:
            return (result[len(result) // 2 - 1] + result[len(result) // 2]) / 2
        else:
            return result[len(result) // 2]
