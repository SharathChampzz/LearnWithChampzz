# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        start_node = None
        result = None

        """
            342
            465
        ----------
            807
        """

        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            right_num = carry % 10
            carry = carry // 10

            if not start_node:
                start_node = ListNode(right_num)
                result = start_node
            else:
                result.next = ListNode(right_num)
                result = result.next

        return start_node