class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x,y = 0,0
        l = len(nums)

        # x will be current index and y will be the fast pointer
        
        # fast pointer will look for non-zero, and it will updated on the current index
        while y < l:
            if nums[y] != 0:
                nums[x] = nums[y]
                x += 1

            y += 1

        # fill out the remaining zeroes
        while x < l:
            nums[x] = 0
            x += 1