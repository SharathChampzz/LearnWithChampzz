class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            print(f'Left: {nums[left]}  Right: {nums[right]}')
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # To check if element exists in left or right part, we need to know which part is sorted
            # Once we know, list is sorted we can check if the elemented exists in that range or not

            # as we know array is sorted, we can conclude left array is sorted
            if nums[left] <= nums[mid]:
                print('Left array is sorted')
                # check if element still falls in the left side or it is in the right side
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1 # element doesnot fall in the first part
            else:
                print('Right array is sorted')
                # check if element still falls in the right side or it is in the right side
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
