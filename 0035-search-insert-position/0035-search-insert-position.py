class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)

        left, right = 0, length-1

        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid # if it is found return that index

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left # left index will hold the next possible insertion for the given target