class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        result = []

        def back_tracking(path: list, chars: list):
            if len(path) == l:
                result.append(path)
                return
            
            for i in chars:
                back_tracking(path + [i], [c for c in chars if c != i])
                
                
        back_tracking(path=[], chars=nums)

        return result