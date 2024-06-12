class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums)
        if k > length: return 0

        # take the sum of the first window
        max_sum = current_sum = sum(nums[0:k])

        # configure next window
        w_start = 1
        w_end = k

        while w_end < length:
            current_sum += nums[w_end] - nums[w_start-1]
            max_sum = max(max_sum, current_sum)

            w_start += 1
            w_end += 1

        return max_sum / k
