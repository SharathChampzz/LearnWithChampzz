class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        mappings = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        for key, value in mappings.items():
            if num >= key:
                roman_char = value*(num//key)
                reminder = num % key
                if reminder:
                    result = roman_char + self.intToRoman(reminder)
                else:
                    result = roman_char
                break
        
        return result
