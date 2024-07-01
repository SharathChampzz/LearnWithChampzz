class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # same question as previous, just that k == 1 in this condition and we need to subtract 1 from the result, as we are deleting 0 from the list and not swapping.
        right = 0
        length = len(nums)
        max_size = 0
        k = 1

        for left in range(length):

            while right < length and (nums[right] or k):
                if nums[right] == 0:
                    k -= 1
                right += 1

            max_size = max(max_size, right-left)
            # print(f'Max Size: {max_size}, left:{left} and right:{right}')

            if nums[left] == 0:
                k += 1 # the first number was 0 and we must have swapped and decremented k value

            if right >= length:
                break

        return max_size-1