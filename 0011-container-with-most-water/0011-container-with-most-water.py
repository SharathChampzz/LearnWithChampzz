class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        length = len(height)
        left = 0
        right = length - 1

        while left < right:
            current_area = min(height[left], height[right])*(right-left)
            print(current_area)
            max_water = max(current_area, max_water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water