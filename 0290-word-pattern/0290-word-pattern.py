class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        words = s.split()

        # there is no full match
        if len(pattern) != len(words):
            return False
        
        for index, char in enumerate(pattern):
            
            # if pattern encountered for the first time, add the mapping
            if char not in mapping:
                
                # check if pattern is already mapped to some other word
                if words[index] in mapping.values():
                    return False
                mapping[char] = words[index]
                
            else:
                if mapping[char] != words[index]:
                    return False

        return True
                
        