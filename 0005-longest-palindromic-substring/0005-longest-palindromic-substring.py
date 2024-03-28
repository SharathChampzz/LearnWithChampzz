class Solution:
    def longestPalindrome(self, s: str) -> str:
        total = len(s)
        result = ""
        max_len = 0

        for start in range(total):
            for end in range(total, -1, -1):
                
                if s[start] != s[end-1]:
                    continue
                p = s[start:end]
                if p == p[::-1]:
                    len_substring = end - start + 1
                    if len_substring > max_len:
                        result = p
                        max_len = len_substring
                    break

        return result
