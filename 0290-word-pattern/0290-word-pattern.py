class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        visited = set() # or we can have char_to_word or word_to_char mapping
        
        s = s.split(' ')
        s_len  = len(s)

        if s_len != len(pattern):
            return False

        for index, char in enumerate(pattern):
            if char not in mapping:

                if s[index] in visited:
                    return False

                mapping[char] = s[index]
                visited.add(s[index])

            else:
                if mapping[char] != s[index]:
                    return False

        return True