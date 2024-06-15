# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge cases: Empty list or single node
        if not head or not head.next: # if length == 0 or length == 1
            return None

        # Use two pointers: slow and fast
        slow = head
        fast = head
        prev = None

        # Traverse the list with slow moving one step at a time and fast moving two steps at a time
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # When fast reaches end slow will be exactly at center
        # remove that by using prev node
        if prev:
            prev.next = prev.next.next

        return head


# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         temp = head

#         length = 1
#         while temp.next:
#             length += 1
#             temp = temp.next

#         if length == 1:
#             return None

#         if length == 2:
#             head.next = None
#             return head

#         jump_time = length // 2

#         temp = head # move the pointer back to head

#         while jump_time > 1:
#             temp = temp.next
#             jump_time -= 1
        
#         # remove middle node
#         temp.next = temp.next.next

#         return head
