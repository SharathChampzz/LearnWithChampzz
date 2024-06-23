# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            guess_status = guess(mid)

            if guess_status == 1:
                print(f'Your guess is {mid} but number is higher than that')
                left = mid + 1
            elif guess_status == -1:
                print(f'Your guess is {mid} but number is lower than that')
                right = mid - 1
            else:
                return mid

        return left # or right