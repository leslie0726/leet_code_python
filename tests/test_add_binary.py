from algorithms.add_binary import Solution


def test_add_binary_success():
    obj=Solution()
    assert obj.addBinary('11','1') == '100'
