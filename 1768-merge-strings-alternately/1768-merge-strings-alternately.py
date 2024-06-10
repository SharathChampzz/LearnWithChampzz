class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        result = ''
        len1 = len(word1)
        len2 = len(word2)

        min_len = min(len1, len2)

        while i < min_len:
            result += word1[i] + word2[i]
            i += 1

        if len1 > min_len:
            while i < len1:
                result += word1[i]
                i += 1
        else:
            while i < len2:
                result += word2[i]
                i += 1

        return result