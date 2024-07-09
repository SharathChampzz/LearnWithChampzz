class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)

        if length == 1:
            return cost[0]
        # if length == 2:
        #     return cost[1] => This will be not correct when cost = [1,100]

        lower_step, upper_step = cost[0], cost[1]

        for i in range(2, length):
            temp = upper_step
            upper_step = min(lower_step, upper_step) + cost[i]
            lower_step = temp

        return min(lower_step, upper_step)

