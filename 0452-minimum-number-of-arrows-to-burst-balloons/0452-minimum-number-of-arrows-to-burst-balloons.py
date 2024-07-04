class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort points by their end coordinates
        points.sort(key=lambda x: x[1])
        
        arrow_count = 1
        end = points[0][1]

        for i in range(1, len(points)):
            start, new_end = points[i]

            if start > end:
                arrow_count += 1
                end = new_end
        
        return arrow_count
