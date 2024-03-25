class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # This is ~ O(n^2) => for loops and finding indexes
        # for index, num in enumerate(nums):
        #     remaining = target - num
        #     if remaining in nums and nums.index(remaining)!=index:
        #         return [index, nums.index(remaining)]

        # O(n) => for loop and find elements in dict takes O(1) on avg
        already_found = {}
        for index, num in enumerate(nums):
            remaining = target - num
            if remaining in already_found:
                return [already_found[remaining], index]
            already_found[num] = index
        