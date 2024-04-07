class Solution:
    def isValid(self, s: str) -> bool:
        bracket_mapping = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []

        for char in s:
            if char in bracket_mapping:
                if not stack:
                    return False
                if stack.pop() != bracket_mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack
