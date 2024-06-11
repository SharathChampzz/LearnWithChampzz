class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ocurrence = []
        result = 0

        for num in nums:
            if num > k: # it is given that k and num are both positives in constraint
                continue
                
                
            remaining = k - num

            
            # print(f'{remaining} found? : {remaining in ocurrence}')
            # check if remaining as already occured
            if remaining in ocurrence:
                result += 1
                ocurrence.remove(remaining) # lets remove after we found pair
            else:
                ocurrence.append(num)
 
        return result