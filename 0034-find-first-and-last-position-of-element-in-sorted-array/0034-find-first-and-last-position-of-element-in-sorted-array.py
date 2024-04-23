class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to find the leftmost occurrence of target
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid  # Found leftmost occurrence
                    else:
                        right = mid - 1  # Continue searching left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1  # Target not found

        # Helper function to find the rightmost occurrence of target
        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid  # Found rightmost occurrence
                    else:
                        left = mid + 1  # Continue searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1  # Target not found

        # Find leftmost and rightmost occurrences
        leftmost = findLeft(nums, target)
        rightmost = findRight(nums, target)

        return [leftmost, rightmost]