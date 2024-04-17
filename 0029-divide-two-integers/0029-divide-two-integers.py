class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        result = 0

        negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend),abs(divisor)

        while dividend >=  divisor:
            temp_divisor, count = divisor, 1

            while (temp_divisor << 1) <= dividend:
                temp_divisor <<= 1
                count <<= 1
            
            dividend -= temp_divisor
            result += count
            
        if negative:
            result = -result

        return result