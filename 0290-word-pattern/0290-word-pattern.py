class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        words = s.split()

        if len(pattern) != len(words):
            return False
        
        for index, char in enumerate(pattern):
            if char not in mapping:
                if words[index] in mapping.values():
                    return False
                mapping[char] = words[index]
            else:
                if mapping[char] != words[index]:
                    return False

        return True
                
        