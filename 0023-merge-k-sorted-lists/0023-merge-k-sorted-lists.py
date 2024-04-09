# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge2List(l1, l2):
            dummy = ListNode()
            current = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1, current = l1.next, current.next
                else:
                    current.next = l2
                    l2, current = l2.next, current.next

            current.next = l1 if l1 else l2

            return dummy.next

        result = None
        for i in range(len(lists)):
            result = merge2List(result, lists[i])

        return result



