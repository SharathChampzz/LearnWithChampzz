class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        We are going to perform XOR here, as we need to indentify the element which doesnot have duplicate of it.
        Because, in XOR, If A and B are same.. we will get output 0, If A and are B, we will get output 1

        TakeAway: You can perform bitwise operations on set of numbers and order doesnot matter. So duplicate number will get
        cancelled, and only unique number stays at the end.
        """
        result = 0
        for i in nums:
            result ^= i

        return result

        # # Using extra space via hashmap set
        # visited = set()
        # for i in nums:
        #     if i not in visited:
        #         visited.add(i)
        #     else:
        #         visited.remove(i)

        # return visited.pop()

        