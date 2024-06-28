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
         
        req_combination_len = len(digits)

        def back_track(path: str, current_digit_index: int):
            if len(path) == req_combination_len:
                result.append(path)
                return
            
            digit = digits[current_digit_index]
            for char in phone_mapping[digit]:
                back_track(path + char, current_digit_index+1)

        back_track('', 0)
        
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
