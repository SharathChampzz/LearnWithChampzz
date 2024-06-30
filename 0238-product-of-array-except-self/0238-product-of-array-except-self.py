class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        # Calculate prefix products
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        # Calculate suffix products
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        return [prefix[i] * suffix[i] for i in range(n)]



"""
Given: [1,2,3,4]

Prefix: [1, 1, 2, 6]
Suffix: [24, , 12, 4, 1]
Multiply: [24, 12, 8, 6]
"""