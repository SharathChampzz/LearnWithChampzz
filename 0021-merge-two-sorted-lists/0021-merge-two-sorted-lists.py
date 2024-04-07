# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        start = dummy_node

        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:  # Combine the conditions for less or equal values
                    start.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    start.next = ListNode(list2.val)
                    list2 = list2.next
                start = start.next  # Moved outside of the if-else block
            elif list1:
                start.next = list1
                break
            else:
                start.next = list2
                break

            # start = start.next  # Moved outside of the if-elif-else block

        return dummy_node.next
