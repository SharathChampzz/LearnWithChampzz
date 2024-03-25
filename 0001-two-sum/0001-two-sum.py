class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """        
        item_count = len(nums)
        for i in range(item_count):
            for j in range(item_count):
                if i == j:
                    continue
                if (nums[i] + nums[j]) == target:
                    return [i,j]
        