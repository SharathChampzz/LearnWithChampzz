class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        prev = None

        for i in nums:
            if i != prev:
                nums[count] = i
                count += 1
            prev = i

        return count