from algorithms.dynamic_programming_solution import Solution


def test_dynamic_programming_solution_successful():
    obj = Solution()
    assert obj.climbStairs(2) == 2
    assert obj.climbStairs(3) == 3
    assert obj.climbStairs(4) == 5
