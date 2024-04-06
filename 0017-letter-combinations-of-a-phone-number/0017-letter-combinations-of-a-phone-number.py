class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

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
            # If the current path is of the same length as the input digits, add it to the result
            if len(path) == len(digits):
                combinations.append(''.join(path))
                return

            # Get the letters corresponding to the current digit
            letters = phone_mapping[digits[index]]

            # Iterate through each letter and recursively backtrack
            for letter in letters:
                path.append(letter)  # Add the letter to the current path
                backtrack(index + 1, path)  # Recur with the next digit
                path.pop()  # Backtrack by removing the added letter

        combinations = []  # List to store the combinations
        backtrack(0, [])  # Start the backtracking from index 0 with an empty path
        return combinations


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
