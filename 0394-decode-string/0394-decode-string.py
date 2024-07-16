class Solution:
    def decodeString(self, s: str) -> str:
        # length = len(s)
        stack = []
        result_str = ""
        """
        Logic:
            Iterate through the string and push the char to the stack until we find the closing bracket
            Once closing bracket is encountered, Now we can solve the problem by poping the characters
            Build the last substring by poping till '['
            Build the last number too and find the substr answer wiz (number*substring)
            So either we got full answer or substring answer, Add this result to stack again at once, so that it will be usefull for next calculation
        """
        for char in s:
            if char != ']':
                stack.append(char)
                
            else:
                # pop it until you get open bracket and build substring
                sub_str = ""
                while stack and (stack[-1] != '['):
                    sub_str = stack.pop() + sub_str
                stack.pop() # remove '['

                # parse the number
                num_str = ''
                while stack and stack[-1].isdigit():
                    num_str = stack.pop() + num_str
                num = int(num_str)
                
                # sub_str result
                result_str = num*sub_str
                print(f'result_str => {result_str}')
                
                # add the substring to stack after solving the subproblem
                stack.append(result_str)

        # stack will be having results from [sub_string, sub_string, sub_string]
        result = ""
        while stack:
            result = stack.pop() + result
        return result
