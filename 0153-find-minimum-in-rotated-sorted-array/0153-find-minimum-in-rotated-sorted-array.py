class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)

        left, right = 0, length - 1

        while left < right:
            mid = (left + right) // 2
            
            if nums[left] < nums[right]:
                return nums[left] # It means array is sorted

            elif nums[mid] < nums[right]: # second part is sorted
                right = mid # result can be mid itself or the left part. So move the pointer to mid

            else:
                left = mid + 1 # left part is sorted but the whole array is not sorted, so the answer must be present in second half. it cant be mid

        return nums[left]