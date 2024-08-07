class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1

        while pointer >= 0:
            # if lsb is less than 9, just add 1 and exit, no need of further processing. Because it will be single digit even after adding 1 to it
            if digits[pointer] < 9:
                digits[pointer] += 1
                return digits

            # if we are here, it means lsb == 9, sum will be 10, thus, set 0 and in next iteration add one again
            digits[pointer] = 0
            pointer -= 1

        digits.insert(0, 1) 

        return digits



        