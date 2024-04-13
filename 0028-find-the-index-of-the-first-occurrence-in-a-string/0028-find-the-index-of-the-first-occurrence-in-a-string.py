class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(haystack)
        
        def check_string_match(start_index):
            for char in needle:
                if start_index >= length or char != haystack[start_index]:
                    return False
                start_index += 1
            return True

        for i in range(length):
            if haystack[i] == needle[0]:
                status = check_string_match(i)
                if status:
                    return i

        return -1