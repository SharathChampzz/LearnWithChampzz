class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        arrow_count = 0
        n = len(points)
        i = 0

        while i < n:
            x, y = points[i] # starting range
            # print(f'x:{x} , y:{y}')

            while i < n - 1:
                i += 1
                new_x, new_y = points[i] # new range

                # check for overlap:
                if new_x >= x and new_x <= y: # There is overlap, new_x is between the starting range
                    
                    x, y = [new_x, y if new_y > y else new_y] # merged one or this will be a new starting range to check from
                    # print(f'(x,y) == {x},{y}')
                else:
                    break
            else:
                i += 1 # the last loop, we dont have 

            arrow_count += 1

        return arrow_count
