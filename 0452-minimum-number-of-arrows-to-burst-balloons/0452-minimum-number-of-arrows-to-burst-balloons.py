class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()

        arrow_count = 0
        n = len(points)
        i = 0

        while i < n:
            x, y = points[i]
            # print(f'x:{x} , y:{y}')

            while i < n - 1:
                i += 1
                new_x, new_y = points[i]

                # check for overlap:
                if new_x >= x and new_x <= y: # not sure if we should consider if ending matches <= or just <
                    if new_y < y:
                        y = new_y # if y is less, then merged interval will be this one
                    x, y = [new_x, y]
                    print(f'(x,y) == {x},{y}')
                else:
                    break
            else:
                i += 1 # the last loop, we dont have 

            arrow_count += 1

        return arrow_count
