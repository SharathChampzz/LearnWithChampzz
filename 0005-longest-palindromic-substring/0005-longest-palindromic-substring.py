class Solution:
    def longestPalindrome(self, s: str) -> str:
        total = len(s)
        result = ""

        for start in range(total):
            for end in range(total, -1, -1):
                p = s[start:end]
                if p == p[::-1]:
                    if len(p) > len(result):
                        result = p
                    break

        return result