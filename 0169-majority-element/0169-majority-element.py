class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        req_len = len(nums) // 2
        occurence = defaultdict(int)

        for i in nums:
            occurence[i] += 1

            if occurence[i] > req_len:
                return i

    def boyerMoore(nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
