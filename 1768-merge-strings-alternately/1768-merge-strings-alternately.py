class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""
        i, j = 0, 0
        len1 = len(word1)
        len2 = len(word2)
        
        while i < len1 and j < len2:
            merged_string += word1[i] + word2[j]
            i += 1
            j += 1

        # Append the remaining characters of the longer string
        merged_string += word1[i:]
        merged_string += word2[j:]

        return merged_string