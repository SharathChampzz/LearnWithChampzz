class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # sort it based on the end range, so that we can get more space for other intervals
        intervals.sort(key= lambda x: x[1])
        

        removed_count = 0
        prev = -float('inf')

        for interval in intervals:
            if interval[0] < prev:
                removed_count += 1
                continue

            prev = interval[1]

        return removed_count