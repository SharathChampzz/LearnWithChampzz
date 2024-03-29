class Solution:
    def reverse(self, x: int) -> int:    
        negative = x < 0

        x = abs(x)

        # reverse = int(str(x)[::-1])
        # result = -reverse if negative else reverse
        
        reverse = 0
        while x:
            reverse = reverse * 10 + x % 10
            x = x // 10
            
        if negative:
            reverse *= -1
        
        if reverse >= 2**31-1 or reverse <= -2**31:
            return 0

        return reverse
        