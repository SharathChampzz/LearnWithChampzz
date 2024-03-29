class Solution:
    def reverse(self, x: int) -> int:    
        negative = x*-1 > 0

        if negative:
            x *= -1

        reverse = int(str(x)[::-1])
        result = -reverse if negative else reverse

        if result >= pow(2,31)-1 or result <= pow(-2, 31):
            return 0

        return result
        