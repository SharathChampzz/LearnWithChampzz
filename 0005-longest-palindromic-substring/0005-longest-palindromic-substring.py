class Solution:
    def longestPalindrome(self, s: str) -> str:
        total = len(s)
        result = ""
        max_length = 0  # Variable to store the length of the longest palindrome found

        for start in range(total):
            # Optimize end range to start from the maximum possible length of palindrome
            for end in range(total, start + max_length, -1):
                # Check if the end characters are same, else there is no need to proceed further
                if s[start] != s[end-1]:
                    continue
                # Check if the substring is a palindrome and longer than the current result
                if s[start:end] == s[start:end][::-1] and end - start > max_length:
                    result = s[start:end]
                    max_length = end - start  # Update max_length with the new longest palindrome length
                    break

        return result
