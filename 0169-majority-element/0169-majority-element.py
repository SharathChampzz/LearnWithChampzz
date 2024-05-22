class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        req_len = len(nums) // 2
        occurence = defaultdict(int)

        for i in nums:
            occurence[i] += 1

            if occurence[i] > req_len:
                return i

