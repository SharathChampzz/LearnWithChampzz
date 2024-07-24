# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using Floyd's cycle-finding algorithm
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def hasCycleUsingExtraAttr(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False # handle empty list

        # lets add visited attribute to check if we are revisiting the node
        while head.next and not hasattr(head.next, 'visited'):
            head = head.next
            head.visited = True # doesnot matter if it is True or False, we just check if we set this attribute

        return True if head.next else False