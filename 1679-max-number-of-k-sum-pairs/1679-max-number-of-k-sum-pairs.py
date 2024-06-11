class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        freq = defaultdict(int)

        for num in nums:
            complement = k - num
            if freq[complement] > 0:
                count += 1
                freq[complement] -= 1
            else:
                freq[num] += 1

        return count