class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        prev_prev = None
        count = 0

        for i in nums:
            if not (i == prev and i == prev_prev): # Check if occurance is not more than 2
                nums[count] = i
                count += 1
            
            prev_prev = prev
            prev = i

        return count
