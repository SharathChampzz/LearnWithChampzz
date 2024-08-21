class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        result = []

        start = end = index = 0

        while index < n:

            # check for continuity
            if (index < n-1) and nums[index + 1] == (nums[end] + 1):
                end += 1
            else:
                if start == end:
                    result.append(str(nums[end]))
                else:
                    result.append(f'{nums[start]}->{nums[end]}')

                start = end = end + 1

            index += 1

        return result
