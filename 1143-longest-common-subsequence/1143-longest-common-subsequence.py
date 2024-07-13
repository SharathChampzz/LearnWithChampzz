class Solution:
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        
        # Create a 2D array with (m+1) x (n+1) dimensions
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 
                    # if char matches read the value diagonally and one to it
                    # because, when the char matches. We will have to start looking at next character from both of the texts
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # if char doesnot match take max of left and top element
        
        # The answer is in the bottom-right cell of the DP table
        return dp[m][n]