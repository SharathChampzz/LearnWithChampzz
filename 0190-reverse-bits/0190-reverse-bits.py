class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        # get each bit from right side, left shift it to reverse it and perform OR logic to update the result
        for i in range(32):
            lsb = (n >> i) & 1
            result = result | (lsb << (31 - i))

        return result