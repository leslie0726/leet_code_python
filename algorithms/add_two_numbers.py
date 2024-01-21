from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        pass

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        tail = dummy_head
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            l1_val = l1.val if l1 != None else 0
            l2_val = l2.val if l2 != None else 0
            sum = l1_val + l2_val + carry
            new_node = ListNode(sum % 10)
            carry = sum // 10
            tail.next = new_node
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            tail = tail.next;
        result = dummy_head.next
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
