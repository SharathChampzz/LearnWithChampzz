class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def back_track(path: list, current_index: int):
            if len(path) == k:
                if sum(path) == n:
                    result.append(path)
                return
            
            for i in range(current_index, 10):
                back_track(path + [i], i+1)
                
        back_track([], 1)

        return result