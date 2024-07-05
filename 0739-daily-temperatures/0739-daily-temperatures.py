class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we are asked to get next greater element, So we will use monotonic decreasing stack. 
        # Idea is, Until you find greater element for a number, Keep it in list and once you get compare and get result 
        # Remember, This the not the next greater element (When we sort) Instead a number which is greater when we iterate from left to right
        # Whenever you encounter big number, we will tell the lower numbers that the current number is bigger than you, and update the answer
        # if we are not finding bigger number, we will add them to the waiting list (stack)
        n = len(temperatures)
        result = [0] * n
        stack = []

        for index, i in enumerate(temperatures):
            if not stack:
                stack.append((index, i))
                continue

            while stack and stack[-1][1] < i:
                old_index, old_value = stack.pop()
                result[old_index] = index - old_index

            stack.append((index, i))

        return result
