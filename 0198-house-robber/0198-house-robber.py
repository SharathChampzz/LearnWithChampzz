class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        The idea is to find the maximum amount of money that can be stolen from a 
        series of non-neighboring houses. 

        We achieve this by keeping track of the two maximum possible loots at any 
        point. There are two choices for each house: pick it or skip it.

        * Picking the current house means skipping the previous one. The new loot 
        becomes the sum of the loot from the house two houses before (n-2) and the 
        current house (n).

        * Skipping the current house means keeping the maximum loot from the previous 
        house (n-1).

        Whichever choice results in the larger amount becomes the new maximum 
        possible loot so far.
        """

        length = len(nums)

        if length < 3:
            return max(nums) # max of 1 or 2 house

        # If we are here, It means there is atleast 3 house
        
        # Store max loot calculation for first and second house, So that we can use it from the third house
        n_2, n_1 = nums[0], max(nums[0], nums[1])

        # calculation from third house
        for i in range(2, length):
            temp = n_1
            n_1 = max(n_2 + nums[i], n_1)
            n_2 = temp

        return n_1
        

    def rob_using_backtrack(self, nums: List[int]) -> int:
        length = len(nums)
        result = 0

        def back_track(start_index, current_sum):
            nonlocal result
            if start_index >= length:
                result = max(result, current_sum)
                return

            for i in range(start_index, length):
                back_track(i + 2, current_sum + nums[i])

        back_track(0, 0)

        return result

# solution = Solution()
# solution.rob([2,7,9,3,1])