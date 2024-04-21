class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []  # Initialize an empty stack to store indices of opening parentheses
        max_len = 0
        start = -1  # Initialize the start index of the current valid substring
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # Push index onto the stack for opening parenthesis '('
            else:
                if stack:  # If stack is not empty (there are unmatched opening parentheses)
                    stack.pop()  # Pop the top index as we encountered a closing parenthesis ')'

                    if stack:  # If stack is not empty after popping
                        max_len = max(max_len, i - stack[-1])  # Update max_len with the current valid substring length
                    else:
                        max_len = max(max_len, i - start)  # Update max_len if stack becomes empty
                else:
                    start = i  # Update the start index of the next potential valid substring
        
        return max_len
