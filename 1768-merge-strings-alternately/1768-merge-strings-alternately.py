class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            merged_string += word1[i]
            merged_string += word2[j]
            i += 1
            j += 1

        # Append the remaining characters of the longer string
        merged_string += word1[i:]
        merged_string += word2[j:]

        return merged_string