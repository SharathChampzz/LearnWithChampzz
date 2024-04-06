from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()  # Sort the input list to simplify the search logic.

        # Define a function to find three numbers that sum up to a target.
        def three_sum(start_index: int, first_value: int) -> List[List[int]]:
            tmp_result = []  # Temporary result list to store valid triplets.
            three_sum_target = target - first_value  # Calculate the target for three-sum.

            # Iterate through the list starting from the given index.
            while start_index < len(nums):
                # Skip duplicates except for the first occurrence after the initial index.
                if start_index != index + 1 and nums[start_index] == nums[start_index - 1]:
                    start_index += 1
                    continue

                left, right = start_index + 1, len(nums) - 1  # Initialize left and right pointers.

                # Use two-pointer technique to find pairs summing up to the three-sum target.
                while left < right:
                    total = nums[start_index] + nums[left] + nums[right]

                    if total == three_sum_target:  # Found a valid triplet.
                        tmp_result.append([first_value, nums[start_index], nums[left], nums[right]])

                        # Skip duplicates for left and right pointers.
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1  # Move left pointer to the next unique value.
                        right -= 1  # Move right pointer to the next unique value.
                    elif total < three_sum_target:  # Adjust pointers based on the total sum.
                        left += 1
                    else:
                        right -= 1

                start_index += 1  # Move to the next index to consider for three-sum.

            return tmp_result

        # Iterate through the list to find the first value of the four-sum.
        for index, i in enumerate(nums[:-3]):
            if index != 0 and nums[index] == nums[index - 1]:  # Skip duplicates.
                continue
            temp_result = three_sum(start_index=index + 1, first_value=i)
            result.extend(temp_result)  # Add valid triplets to the result list.
            
        return result  # Return the final result containing all valid quadruplets.
