class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        So in this problem, number can appear can thrice or for once. We need to indentify that number which appeared once. 
        Basically, we will have to eliminate those duplicate numbers. 

        We can use hashmap or sort and group or bit manupulation.

        We are using bit count method here
        """
        bit_counts = [0] * 32
    
        for num in nums:
            for i in range(32):
                bit_counts[i] += (num >> i) & 1
        
        result = 0
        for i in range(32):
            if bit_counts[i] % 3 != 0:
                if i == 31:  # handle negative numbers
                    result -= (1 << i)
                else:
                    result |= (1 << i)
        
        return result
        