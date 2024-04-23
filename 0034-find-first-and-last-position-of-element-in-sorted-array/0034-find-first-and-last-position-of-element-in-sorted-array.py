class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        
        def binary_search():
            left = 0
            right = length-1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid

                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        index = binary_search()

        if index == -1:
            return [-1,-1]

        left = right = index

        while left > 0 or right < length-1:
            prev_left, prev_right = left, right
            if left > 0 and nums[left-1] == target:
                left -= 1
            if right < length-1 and nums[right+1] == target:
                right += 1
            
            # if left and right values are not modified, then we can stop here
            if prev_left == left and prev_right == right:
                break

        return [left, right]