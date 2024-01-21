from typing import List

class solution:
    def __init__(self):
        pass
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# if __name__ == '__main__':
#     nums = [2,7,11,15]
#     twoSum(nums,9)
#     nums = [3,2,4]
#     twoSum(nums,6)
#     nums = [3,3]
#     twoSum(nums,6)
