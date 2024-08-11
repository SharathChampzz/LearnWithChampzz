class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        total_nums = len(nums)

        # initialize the DB array
        longest = [1] * total_nums # atleast 1 will be the length for any index

        # from the end fill up the DB array
        # total_nums - 2 should be fine, for total_nums - 1, j loop will anyways not run
        for i in range(total_nums - 2, -1, -1):
            # read all the next available greater nums and its longest values
            next_max = 0
            for j in range(i+1, total_nums):
                if nums[j] > nums[i]:
                    next_max = max(next_max, longest[j])

            longest[i] += next_max  # nothing but 1 + max of next greatest length

        return max(longest)


