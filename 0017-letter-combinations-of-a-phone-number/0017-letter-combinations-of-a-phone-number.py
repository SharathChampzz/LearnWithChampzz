# from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        chars = [digit_to_letters[digit] for digit in digits]

        def get_combination(los: List[str]) -> List[str]:
            result = []

            if len(los) == 1:
                return list(los[0])
            else:
                temp = get_combination(los[1:])
                for char in los[0]:
                    result.extend([char + x for x in temp])
                return result

        final_combination = get_combination(chars)
        return final_combination
