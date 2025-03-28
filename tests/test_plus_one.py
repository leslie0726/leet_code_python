from algorithms.plus_one import Solution


def test_plus_one_success():
    obj = Solution()
    assert obj.plusOne([1,2,4]) == [1,2,5]
    assert obj.plusOne([4,3,2,1]) == [4,3,2,2]
    assert obj.plusOne([9]) == [1,0]
    assert obj.plusOne([9,8,7,6,5,4,3,2,1,0]) == [9,8,7,6,5,4,3,2,1,1]