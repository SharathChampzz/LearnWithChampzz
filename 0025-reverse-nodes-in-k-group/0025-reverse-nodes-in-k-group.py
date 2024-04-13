# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        # Helper function to reverse a sublist
        def reverse_sublist(start, end):
            prev = None
            curr = start
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            # Find the end of the k-group
            group_end = prev_group_end
            for _ in range(k):
                group_end = group_end.next
                if not group_end:
                    return dummy.next
            
            # Reverse the current k-group
            group_start = prev_group_end.next
            next_group_start = group_end.next
            group_end.next = None
            prev_group_end.next = reverse_sublist(group_start, group_end) # prev group to reversed new head node
            group_start.next = next_group_start # group_start will be the tail after reverse, so point group_start to the next group
            
            # Update pointers for the next iteration
            prev_group_end = group_start

        return dummy.next