class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        while n > 0:
            carry = n % 2
            n = n // 2

            if carry:
                result += 1

        return result