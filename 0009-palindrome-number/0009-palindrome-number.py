class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False # negative

        if x < 10:
            return True # single digit

        original_num = x
        reversed_num = 0

        while x:
            last_digit = x % 10
            reversed_num = reversed_num * 10 + last_digit
            x = x // 10
            
        return original_num == reversed_num