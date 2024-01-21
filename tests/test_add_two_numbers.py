from algorithms.add_two_numbers import Solution,ListNode



def test_two_sum_success():
    obj = Solution()
    l1 = obj.to_list_node([2,4,3])
    l2 = obj.to_list_node([5,6,4])
    assert obj.to_array(obj.addTwoNumbers(l1,l2)) == [7,0,8]

    l1 = obj.to_list_node([0])
    l2 = obj.to_list_node([0])
    assert obj.to_array(obj.addTwoNumbers(l1, l2)) == [0]

    l1 = obj.to_list_node([9,9,9,9,9,9,9])
    l2 = obj.to_list_node([9,9,9,9])
    assert obj.to_array(obj.addTwoNumbers(l1, l2)) == [8,9,9,9,0,0,0,1]

    l1 = obj.to_list_node([9,9,1])
    l2 = obj.to_list_node([1])
    assert obj.to_array(obj.addTwoNumbers(l1, l2)) == [0,0,2]

    l1 = obj.to_list_node([5])
    l2 = obj.to_list_node([5])
    assert obj.to_array(obj.addTwoNumbers(l1, l2)) == [0,1]


