# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # We want to know the mid element here so slow and fast pointer is the way to go
        # Once we know the mid element, we want to know previous pair element to calc sum, so lets use stack
        sp = head # slow pointer
        fp = head # fast pointer
        stack = []
        max_sum = 0

        while fp and fp.next:
            stack.append(sp.val)

            sp = sp.next
            fp = fp.next.next

        while sp:
            # curren_val = stack.pop()
            # print(f'Current Calc : {curren_val} + {sp.val} = {curren_val + sp.val}')
            max_sum = max(max_sum, stack.pop() + sp.val)
            sp = sp.next

        return max_sum
