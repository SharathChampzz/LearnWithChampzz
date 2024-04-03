class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        result = []

        for i in range(length):
            if i!=0 and nums[i] == nums[i-1]:
                # number is same as prev, no need of calculating again
                continue

            left = i + 1
            right = length - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # remove consecutive duplicate numbers to avoid the same duplicate calculation
                    while left < right and nums[left+1]==nums[left]:
                        left += 1
                    while left < right and nums[right-1]==nums[right]:
                        right -= 1
                    
                    # do the final increment as next element is not same as the prev
                    left += 1
                    right -= 1

                elif total < 0:
                    # as array is sorted, increment will give us higher number, so that sum of 3 numbers might reach 0
                    left += 1

                else:
                    # similar when total > 0, decrement pointed to look for less number, so that sum would be decreased or might get 0
                    right -= 1

        return result

        # length = len(nums)
        # nums.sort()
        # result = []

        # for index1 in range(length):
        #     first_value = nums[index1]
            
        #     for index2 in range(index1+1, length):
        #         second_value = nums[index2]
        #         third_value = - (first_value + second_value)

        #         if index2+1 < length and third_value in nums[index2+1:]:
        #             temp_result = [first_value, second_value, third_value]
        #             if temp_result not in result:
        #                 result.append(temp_result)

        # return result
