class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the input list for easier comparison
        nums.sort()
        length = len(nums)
        result = float('inf')  # Initialize the result with infinity

        for i in range(length):
            # Skip duplicate numbers to avoid redundant calculations
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = length - 1

            while left < right:
                # Calculate the current sum
                current_sum = nums[i] + nums[left] + nums[right]

                # Update the result if the current sum is closer to the target
                if abs(target - current_sum) < abs(target - result):
                    result = current_sum

                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result
