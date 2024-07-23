class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        left, right = 0, n-1

        while left < right:
            left_char = s[left]
            right_char = s[right]

            if not left_char.isalnum():
                left += 1
            elif not right_char.isalnum():
                right -= 1
            else:
                if left_char.lower() == right_char.lower():
                    left += 1
                    right -= 1
                else:
                    return False

        return True
