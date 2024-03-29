class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        reversed_x = int(str(x)[::-1])
        return x == reversed_x