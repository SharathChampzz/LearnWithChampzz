class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        mappings = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in mappings:
                result += mappings[s[i:i+2]]
                i += 2  # Increment by 2 since we processed 2 characters
            else:
                result += mappings[s[i]]
                i += 1  # Increment by 1 for single characters
                
        return result