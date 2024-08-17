class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [""]

        for folder in path.split('/'):
            if not folder:
                continue

            if folder.isalpha() or len(folder) > 2 or any([char.isalpha() for char in folder]):
                stack.append(folder)
            else:
                pop_count = len(folder) - 1 # ".."
                while stack and pop_count:
                    stack.pop()
                    pop_count -= 1

        result_str = '/'.join(stack)

        return result_str if result_str.startswith('/') else '/' + result_str
