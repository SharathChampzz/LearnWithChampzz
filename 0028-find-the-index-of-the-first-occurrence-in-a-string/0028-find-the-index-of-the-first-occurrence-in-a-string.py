class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:  # Return 0 if needle is an empty string
            return 0
        
        haystack_length = len(haystack)
        needle_length = len(needle)
        
        for i in range(haystack_length - needle_length + 1):
            if haystack[i:i + needle_length] == needle:
                return i
        
        return -1  # Return -1 if needle is not found in haystack
