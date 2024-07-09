class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        lower_step, upper_step = 1, 2

        # we know the answer for step1 and step2 lets use that to build the next steps
        for _ in range(3, n+1):
            temp = upper_step
            upper_step = lower_step + upper_step
            lower_step = temp

        return upper_step

