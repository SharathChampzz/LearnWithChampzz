class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def back_track(so_far: list, start_index: int) -> None:
            if len(so_far) == k:
                result.append(so_far)
                return

            for i in range(start_index, n):
                back_track(so_far + [i+1], i + 1) # [i+1] because it is 0-indexed but answer is 1-indexed

        back_track([], 0)

        return result