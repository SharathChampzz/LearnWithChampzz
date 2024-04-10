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
        
        # there should be atleast 2 more nodes for swapping
        while current.next and current.next.next:
            # read the 3 nodes
            node1, node2, node3 = current.next, current.next.next, current.next.next.next

            # swap the nodes
            current.next, node2.next, node1.next = node2, node1, node3

            # move the current node to the next pair
            current = node1
        
        return dummy.next