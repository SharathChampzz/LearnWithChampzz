# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        # move the head node to the next but before that store it in temp_node
        # point the temp_node to previous
        # update the previous node, So that for the next time, we can point new node to it
        while head:
            temp_node = head
            head = head.next
            temp_node.next = prev
            prev = temp_node

        return prev 
        