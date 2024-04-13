class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(haystack)
        needle_length = len(needle)
        
        def check_string_match(start_index):
            for char in needle:
                if start_index >= length or char != haystack[start_index]:
                    return False
                start_index += 1
            return True

        for i in range(length-needle_length+1):
            if haystack[i:i + needle_length] == needle:
                return i

        return -1