class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def back_track(so_far: list, index: int, total: int) -> None:

            if total > target:
                return

            if total == target:
                result.append(so_far)
                return

            for i in range(index, n):
                back_track(so_far + [candidates[i]], i, total + candidates[i])

        back_track([], 0, 0)

        return result
