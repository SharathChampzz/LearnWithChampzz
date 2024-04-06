class Solution:
    def letterCombinations(self, digits):
        result = []
        
        if not digits:
            return result

        # Define a dictionary mapping digits to their respective letters
        phone_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
         
        def backtrack(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            for char in phone_mapping[digits[index]]:
                backtrack(index+1, path+char)
                
        backtrack(0, "")
        
        return result
                

        # if not digits:
        #     return []

        # digit_to_letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        # chars = [digit_to_letters[digit] for digit in digits]

        # def get_combination(los: List[str]) -> List[str]:
        #     result = []

        #     if len(los) == 1:
        #         return list(los[0])
        #     else:
        #         temp = get_combination(los[1:])
        #         for char in los[0]:
        #             result.extend([char + x for x in temp])
        #         return result

        # final_combination = get_combination(chars)
        # return final_combination
