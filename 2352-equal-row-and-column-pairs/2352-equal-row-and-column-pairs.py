class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = [tuple(i) for i in grid]
        cols = [column for column in zip(*grid)]

        rows_counter = Counter(rows)
        # print(rows_counter)

        pairs = 0

        for col in cols:
            pairs += rows_counter.get(col, 0)
            
        return pairs