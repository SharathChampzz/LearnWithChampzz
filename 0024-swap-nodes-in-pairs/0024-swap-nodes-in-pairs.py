# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = dummy

        # we need atleast two nodes for swapping
        while current.next and current.next.next:
            current_node, node1, node2 = current.next, current.next.next, current.next.next.next

            current.next, node1.next, current_node.next = node1, current_node, node2

            current = current_node
        
        return dummy.next


        