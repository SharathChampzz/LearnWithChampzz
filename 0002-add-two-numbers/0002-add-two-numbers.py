# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def takeSum(self, a, b, carry):
        sum = a + b + carry
        answer = sum % 10
        carry = sum // 10

        return answer, carry

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = temp = ListNode()

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            answer, carry = self.takeSum(a, b, carry)
            temp.next = ListNode(answer)

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next
            temp = temp.next

        return head.next