class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # Sort points by their end coordinates
        points.sort(key=lambda x: x[1])
        
        arrow_count = 0
        last_shot = -float('inf')
        
        for start, end in points:
            if start > last_shot:
                arrow_count += 1
                last_shot = end
        
        return arrow_count
