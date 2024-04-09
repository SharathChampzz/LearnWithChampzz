class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(open_count, close_count, s):
            if open_count == close_count == n:
                result.append(s)
                return

            if open_count < n:
                backtrack(open_count + 1, close_count, s + '(')

            if close_count < open_count:
                backtrack(open_count, close_count + 1, s + ')')

        backtrack(0, 0, '')

        return result