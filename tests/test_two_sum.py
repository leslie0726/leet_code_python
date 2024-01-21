from algorithms.two_sum import solution


def test_two_sum_success():
    obj = solution()
    nums = [2, 7, 11, 15]
    assert obj.twoSum(nums,9) == [0, 1]
    nums = [3,2,4]
    assert obj.twoSum(nums, 6) == [1, 2]
    nums = [3,3]
    assert obj.twoSum(nums, 6) == [0, 1]

def test_two_sum_empty():
    obj = solution()
    nums = [3, 2]
    assert obj.twoSum(nums, 6) == []
