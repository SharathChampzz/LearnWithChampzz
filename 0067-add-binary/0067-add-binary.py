class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0

        result = ''

        while i >= 0 or j >= 0 or carry:
            temp_a = int(a[i]) if i >= 0 else 0
            temp_b = int(b[j]) if j >= 0 else 0
            
            temp_sum = int(temp_a) + int(temp_b) + carry

            unit = temp_sum % 2
            carry = temp_sum // 2

            result = str(unit) + result

            i -= 1
            j -= 1

        return result



        