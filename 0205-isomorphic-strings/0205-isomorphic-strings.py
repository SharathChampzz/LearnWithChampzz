class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()
        visited = set()

        for index, char in enumerate(s):
            if char in mapping:
                if mapping[char] != t[index]: # check if it maps to the existing mapping
                    return False
            elif t[index] in visited: # this is to check if the same char is being tried to map it into another char
                return False
            else:
                mapping[char] = t[index] # add mapping and updated visited chars
                visited.add(t[index])

        return True
        