# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # lets have separate linkedlist to store odd and evens
        # store the head node in temp_nodes. Will be needed to merge later
        odd_list = temp_odd_node = ListNode()
        even_list = temp_even_node = ListNode()
        counter = 1

        while head:
            if counter % 2 != 0: # odd - Add it to odd LL
                odd_list.next = head
                odd_list = odd_list.next
            else: # even - Add it Even LL
                even_list.next = head
                even_list = even_list.next
            counter += 1
            head = head.next

        # At the end, Either odd/even LL is still pointing to the main list
        # To avoid cycle, set the end to None
        odd_list.next = None
        even_list.next = None

        # join odd and even list
        odd_list.next = temp_even_node.next # ignore the first node

        return temp_odd_node.next # ignore the first node