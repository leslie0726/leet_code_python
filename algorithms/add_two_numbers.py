from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        pass

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        result_tmp = result
        increase = 0
        while True:
            if l1 == None and l2 == None:
                if increase == 1:
                    result_tmp.val = 1
                else:
                    result_tmp = None
                break;
            elif l1 == None:
                if l2.val + increase >= 10:
                    result_tmp.val = l2.val + increase - 10
                    increase = 1
                else:
                    result_tmp.val = l2.val + increase
                    increase = 0
                if l2.next != None or increase ==1:
                    result_tmp.next = ListNode()
                result_tmp = result_tmp.next
                l2 = l2.next
            elif l2 == None:
                if l1.val + increase >= 10:
                    result_tmp.val = l1.val + increase - 10
                    increase = 1
                else:
                    print(l1.val + increase)
                    result_tmp.val = l1.val + increase
                    increase = 0
                if l1.next != None or increase ==1:
                    result_tmp.next = ListNode()
                result_tmp = result_tmp.next
                l1 = l1.next
            else:
                if l1.val + l2.val + increase >= 10:
                    result_tmp.val = l1.val + l2.val + increase - 10
                    increase = 1;
                else:
                    result_tmp.val = l1.val + l2.val + increase
                    increase = 0;
                l1 = l1.next;
                l2 = l2.next;
                if l1 == None and l2 == None:
                    if increase == 1:
                        result_tmp.next =ListNode(1)
                    break;
                result_tmp.next = ListNode()
                result_tmp = result_tmp.next;
        return result;

    def to_array(self, list_node) -> List[int]:
        result_array = []
        while True:
            result_array.append(list_node.val)
            if list_node.next == None:
                break;
            list_node = list_node.next
        return result_array

    def to_list_node(self, array: List[int]) -> Optional[ListNode]:
        result = ListNode()
        result_tmp = result
        for i in range(len(array)):
            result_tmp.val = array[i]
            if i != len(array) - 1:
                result_tmp.next = ListNode()
                result_tmp = result_tmp.next
        return result
