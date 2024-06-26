class Solution:
    def countBits(self, n: int) -> List[int]:
        # return [bin(i).count('1') for i in range(n+1)]

        # using dynamic programming
        dp = [0] * (n+1)

        for i in range(n+1):
            dp[i] = dp[i//2]
            
            # if it is odd
            dp[i] += i & 1
            
            # if i%2 != 0:
            #     dp[i] += 1

        return dp